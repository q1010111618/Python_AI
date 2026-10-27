/* ==========================================================================
   汉字谜盒 · 交互逻辑（jQuery）
   ========================================================================== */
$(function () {

  // 版本标记：F12 控制台能看到，用来确认浏览器加载的不是缓存里的旧文件
  console.log('%c汉字谜盒 UI v15（删除会话前弹窗二次确认）', 'color:#7c5cff;font-weight:bold');

  /* 谜题库已移到后端 main.py（RIDDLES），前端不再存一份，避免两边答案不一致 */

  /* ----------------------------- 状态 ----------------------------- */
  var records = [];      // 所有游戏记录
  var currentId = null;  // 当前记录 id

  /* ----------------------------- 图标 ----------------------------- */
  // AI：机器人
  var ICON_BOT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">' +
    '<rect x="4" y="8" width="16" height="11" rx="3.6"></rect>' +
    '<path d="M12 8V4.6"></path><circle cx="12" cy="3.4" r="1.3"></circle>' +
    '<path d="M9.2 12.4v1.6M14.8 12.4v1.6"></path></svg>';

  // 用户：实心人形（比线条图标更醒目，和 AI 机器人一眼区分）
  var ICON_USER = '<svg viewBox="0 0 24 24" fill="currentColor">' +
    '<circle cx="12" cy="8" r="3.7"></circle>' +
    '<path d="M12 13.3c-4 0-6.8 2.2-7.6 5.4-.2.9.5 1.7 1.4 1.7h12.4c.9 0 1.6-.8 1.4-1.7-.8-3.2-3.6-5.4-7.6-5.4z"></path></svg>';

  /* ----------------------------- 工具函数 ----------------------------- */
  function stamp(date) {
    var d = date || new Date();
    var p = function (n) { return n < 10 ? '0' + n : '' + n; };
    return d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate()) +
      '_' + p(d.getHours()) + '-' + p(d.getMinutes()) + '-' + p(d.getSeconds());
  }

  function findRecord(id) {
    for (var i = 0; i < records.length; i++) {
      if (records[i].id === id) { return records[i]; }
    }
    return null;
  }

  function currentRecord() { return findRecord(currentId); }

  /* ----------------------------- 渲染：左侧记录列表 ----------------------------- */
  function renderRecords() {
    var $list = $('#recordList').empty();

    $.each(records, function (_, rec) {
      $('<li>')
        .addClass('record' +
          (rec.id === currentId ? ' active' : '') +
          (rec.loaded ? '' : ' unloaded'))     // 内容还没从后端读过 -> 淡显
        .attr('data-id', rec.id)
        .attr('title', (rec.sessionId || rec.name) +
          (rec.loaded ? '' : '（点击载入聊天记录）'))
        .append($('<span class="time">').text(rec.name))
        .append($('<button class="del" type="button" title="删除记录">').html('&times;'))
        .appendTo($list);
    });
  }

  /* ----------------------------- 渲染：聊天区 ----------------------------- */
  function renderMessages() {
    var rec = currentRecord();
    var $box = $('#messages').empty();

    $('#sessionName').text(rec.name);

    $.each(rec.messages, function (_, msg) {
      appendMessage(msg.who, msg.text, true);
    });

    renderRail();
    scrollToBottom();
  }

  function appendMessage(who, text, silent) {
    var isMe = who === 'me';
    var $msg = $('<div class="msg">').addClass(isMe ? 'me' : 'bot')
      .append($('<div class="avatar">').html(isMe ? ICON_USER : ICON_BOT))
      .append($('<div class="bubble">').text(text));

    $('#messages').append($msg);

    if (!silent) {
      var rec = currentRecord();
      rec.messages.push({ who: who, text: text });
      scrollToBottom();
    }
  }

  /* 答题栏：答对显示“X字”并加红色下划线，答错原样显示 */
  function renderRail() {
    var rec = currentRecord();
    var $rail = $('#answerRail').empty();

    $.each(rec.guesses, function (idx, g) {
      var text = g.text || g.char || '';
      var label = g.right ? text + '字' : text;

      var $chip = $('<div class="rail-chip">')
        .addClass(g.right ? 'hit' : '')
        .append($('<span>').addClass(g.right ? 'mark' : '').text(label));

      var $avatar = $('<button class="rail-avatar" type="button" title="换一道新题">')
        .html(ICON_BOT)
        .attr('data-riddle', g.riddle || '');

      $rail.append($('<div class="rail-item">').append($chip).append($avatar));
    });
  }

  function scrollToBottom() {
    var el = document.getElementById('chatScroll');
    if (el) { el.scrollTop = el.scrollHeight; }
  }

  /* ----------------------------- 出题与答题 ----------------------------- */
  // 出题：发一条空消息，后端发现会话没有当前题目就会出一道新题
  function askRiddle() {
    sendMessage('');
  }

  // 发送：先本地显示用户消息，再调 /api/chat，用后端返回的 reply / guesses 渲染
  function sendMessage(text) {
    var rec = currentRecord();

    // 会话还没建好（页面刚打开、接口还没回来，或建会话失败）：先建会话，建好再补发这条消息
    if (!rec || !rec.sessionId) {
      console.warn('[发送] 会话未就绪（rec=' + !!rec + '），先建会话再补发：', text);
      newGame(text);
      return;
    }

    if (text) { appendMessage('me', text); }   // 立刻上屏，不等接口

    // “思考中”占位气泡：后端要调大模型，实测一轮 4~13 秒，
    // 没有这个占位的话用户会以为点了没反应。拿到回复后立刻移除（不会写进聊天记录）
    var $thinking = $('<div class="msg bot">')
      .append($('<div class="avatar">').html(ICON_BOT))
      .append($('<div class="bubble">').text('AI正在思考…'));
    $('#messages').append($thinking);
    scrollToBottom();

    requestChat(text, function (data, err) {
      $thinking.remove();
      if (err) {
        appendMessage('bot', '（提示：与AI交互失败：' + err + '）');
        return;
      }

      // 后端可能返回两种结构，都兼容：
      //   字符串           → 直接当回复文本（当前占位版就这么返回）
      //   对象 {reply,...} → 取 reply 显示，guesses 有就刷新答题栏
      var reply = typeof data === 'string' ? data : (data && data.reply);
      if (reply) { appendMessage('bot', reply); }

      if (data && data.guesses) {
        rec.guesses = data.guesses;   // 答题栏以后端为准
        renderRail();
      }
    });
  }

  /* ----------------------------- 后端接口 ----------------------------- */
  // 调用后端 /api/session 新建会话（返回 {code, message, data}）
  // callback(sessionId, errMsg)：成功时 sessionId 是字符串、errMsg 为 null；
  // 失败（后端没启动、超时、code 非 200）时 sessionId 为 null，errMsg 是原因，由调用方兜底
  function createSession(callback) {
    $.ajax({
      url: '/api/session',
      type: 'POST',
      dataType: 'json',
      timeout: 5000
    }).done(function (res) {
      if (res && res.code === 200 && res.data) {
        callback(res.data, null);
      } else {
        callback(null, (res && res.message) || '接口返回数据异常');
      }
    }).fail(function (xhr, status, err) {
      console.error('[会话接口失败]', xhr.status, status, err, xhr.responseText);
      callback(null, '接口请求失败：' + (err || status) + '（HTTP ' + xhr.status + '）');
    });
  }

  // 查询历史会话列表（GET /api/sessions）：首页加载时先问一次“有没有历史会话”
  // callback(ids, errMsg)：ids 是会话ID数组（已按时间倒序，第一个即最近一次会话）
  function fetchSessions(callback) {
    $.ajax({
      url: '/api/sessions',
      type: 'GET',
      dataType: 'json',
      timeout: 5000
    }).done(function (res) {
      if (res && res.code === 200 && res.data) {
        // 后端可能返回两种形态：字符串数组 ["id", ...] 或 {sessions:[{session_id}, ...]}，
        // 这里统一归一化成会话ID数组，后端改结构时前端不用跟着改
        var raw = Array.isArray(res.data) ? res.data : (res.data.sessions || []);
        var ids = $.map(raw, function (item) {
          return typeof item === 'string' ? item : (item && item.session_id);
        });
        callback($.grep(ids, function (id) { return !!id; }), null);
      } else {
        callback([], (res && res.message) || '接口返回数据异常');
      }
    }).fail(function (xhr, status, err) {
      console.error('[会话列表接口失败]', xhr.status, status, err, xhr.responseText);
      callback([], '接口请求失败：' + (err || status) + '（HTTP ' + xhr.status + '）');
    });
  }

  // 读取某个会话的完整消息（GET /api/session/{id}），用于首页恢复历史会话
  // callback(data, errMsg)：data 形如 {session_id, messages:[{role, content}]}
  function fetchSession(sessionId, callback) {
    $.ajax({
      url: '/api/session/' + encodeURIComponent(sessionId),
      type: 'GET',
      dataType: 'json',
      timeout: 5000
    }).done(function (res) {
      if (res && res.code === 200 && res.data) {
        callback(res.data, null);
      } else {
        callback(null, (res && res.message) || '接口返回数据异常');
      }
    }).fail(function (xhr, status, err) {
      console.error('[会话详情接口失败]', xhr.status, status, err, xhr.responseText);
      callback(null, '接口请求失败：' + (err || status) + '（HTTP ' + xhr.status + '）');
    });
  }

  // 删除后端会话（DELETE /api/session/{id}）：callback(errMsg)，成功时 errMsg 为 null
  // 只有后端真的删掉了，前端才把这条从列表里移除，避免“刷新后又回来”
  function deleteSession(sessionId, callback) {
    console.log('[请求] DELETE /api/session/' + sessionId);
    $.ajax({
      url: '/api/session/' + encodeURIComponent(sessionId),
      type: 'DELETE',
      dataType: 'json',
      timeout: 5000
    }).done(function (res) {
      if (res && res.code === 200) {
        callback(null);
      } else {
        callback((res && res.message) || '接口返回数据异常');
      }
    }).fail(function (xhr, status, err) {
      console.error('[删除会话接口失败]', xhr.status, status, err, xhr.responseText);
      callback('接口请求失败：' + (err || status) + '（HTTP ' + xhr.status + '）');
    });

  }

  // 调用后端 /api/chat：把消息发给后端，拿回 AI 的回复
  // 注意：后端用 BaseModel 接收，必须发 JSON（contentType + JSON.stringify），
  // 直接用表单格式会报 422 Unprocessable Entity
  function requestChat(text, callback) {
    var rec = currentRecord();
    if (!rec || !rec.sessionId) {
      callback(null, '当前会话没有 sessionId，请点“新建游戏”重新建会话');
      return;
    }

    var payload = { session_id: rec.sessionId, message: text || '' };
    console.log('[请求] POST /api/chat', payload);

    $.ajax({
      url: '/api/chat',
      type: 'POST',
      contentType: 'application/json',
      dataType: 'json',
      data: JSON.stringify(payload),
      // 超时给 60 秒：后端要等大模型生成，实测一轮 4~13 秒，
      // 之前 18 秒在模型变慢时会被浏览器直接掐断，表现为“超时无响应”
      timeout: 60000
    }).done(function (res) {
      console.log('[响应] /api/chat', res);
      if (res && res.code === 200 && res.data) {
        callback(res.data, null);
      } else if (res && res.code === 404) {
        callback(null, '会话已失效：' + res.message);
      } else {
        callback(null, (res && res.message) || '接口返回数据异常');
      }
    }).fail(function (xhr, status, err) {
      console.error('[聊天接口失败]', xhr.status, status, err, xhr.responseText);
      // status === 'timeout' 是等太久被浏览器掐断，单独给一句人话，别显示成 “timeout（HTTP 0）”
      if (status === 'timeout') {
        callback(null, '等待超时（60秒），AI 这会儿有点慢，请稍后再试');
      } else {
        callback(null, '接口请求失败：' + (err || status) + '（HTTP ' + xhr.status + '）');
      }
    });
  }

  /* ----------------------------- 确认弹窗 ----------------------------- */
  // 删除这类不可逆操作先弹窗二次确认：只有点“确认删除”才会回调 onOk
  // 取消方式：点“取消”按钮、点遮罩空白处、按 Esc
  function confirmDialog(title, text, onOk) {
    var $mask = $('<div class="modal-mask">');
    var $modal = $('<div class="modal">')
      .append($('<div class="modal-title">').text(title))
      .append($('<div class="modal-text">').text(text))
      .append($('<div class="modal-actions">')
        .append($('<button class="modal-btn cancel" type="button">').text('取消'))
        .append($('<button class="modal-btn danger" type="button">').text('确认删除')));

    // 关窗时一定要把键盘监听一起解绑，否则每次弹窗都会多留一个监听
    function close() {
      $mask.remove();
      $(document).off('keydown.modal');
    }

    $mask.on('click', function (e) { if (e.target === $mask[0]) { close(); } });
    $modal.find('.cancel').on('click', close);
    $modal.find('.danger').on('click', function () { close(); onOk(); });
    $(document).on('keydown.modal', function (e) {
      if (e.key === 'Escape' || e.keyCode === 27) { close(); }
    });

    $mask.append($modal).appendTo('body');
    // 默认焦点给“取消”：避免手滑按回车直接删掉
    $modal.find('.cancel')[0].focus();
  }

  /* ----------------------------- 记录操作 ----------------------------- */
  function createRecord(name, sessionId) {
    var rec = {
      id: 'r' + Date.now() + Math.floor(Math.random() * 1000),
      name: name || stamp(),
      sessionId: sessionId || '',   // 后端返回的会话ID；接口没通时为空，仅本地记录
      messages: [],
      guesses: [],
      used: [],
      current: null,
      loaded: false   // 会话内容是否已从后端读取（历史会话是点开时才读，避免启动一次性全拉）
    };
    records.unshift(rec);
    currentId = rec.id;
    return rec;
  }

  // pendingText：建好会话后要补发的消息（发送时会话还没就绪会走到这里）
  function newGame(pendingText) {
    var $btn = $('#btnNewGame').prop('disabled', true);   // 请求期间禁用，防重复点击

    createSession(function (sessionId, err) {
      $btn.prop('disabled', false);

      // 接口不通时用本地时间戳兜底，保证游戏照样能玩；接通时直接用后端会话ID当记录名
      var rec = createRecord(sessionId || stamp(), sessionId);
      rec.loaded = true;   // 新建的会话内容就在本地产生，不需要再去后端读
      console.log('[会话] 已创建 ->', rec.sessionId || '(本地兜底，无 sessionId)');

      renderRecords();
      renderMessages();
      //appendMessage('bot', '你好呀！我是汉字谜盒的AI机器人，我们一起来猜字谜吧～');
      if (err) {
        appendMessage('bot', '（提示：新建会话接口未连通，已改用本地记录。原因：' + err + '）');
      }

      // 有补发内容就直接发它，否则出第一道题
      if (pendingText) { sendMessage(pendingText); } else { askRiddle(); }
    });
  }

  function switchRecord(id) {
    if (id === currentId) { return; }
    currentId = id;
    renderRecords();
    renderMessages();

    // 历史会话在列表里全都展示，但内容是点开时才去后端读（懒加载）
    var rec = findRecord(id);
    if (rec && rec.sessionId && !rec.loaded) { loadSessionContent(rec); }
  }

  // 只负责把记录从列表里摘掉并刷新界面（真正的删除动作在 deleteRecord 里）
  function removeRecord(id) {
    records = $.grep(records, function (rec) { return rec.id !== id; });
    if (!records.length) { newGame(); return; }   // 删光了就自动新建一条，保证还能玩
    if (id === currentId) {
      currentId = records[0].id;
      var next = findRecord(currentId);
      // 切到的这条如果还没载入过内容，顺手载入，否则聊天区会是一片空白
      if (next && next.sessionId && !next.loaded) { loadSessionContent(next); }
    }
    renderRecords();
    renderMessages();
  }

  // 真正执行删除：有 sessionId 的先调后端 DELETE /api/session/{id} 删掉服务器上的文件，
  // 删成功才从列表移除；没有 sessionId（接口不通时的本地记录）或删除失败时按本地删除处理
  function doDeleteRecord(rec) {
    // 没有 sessionId：服务器上本来就没这个文件，直接本地删
    if (!rec.sessionId) { removeRecord(rec.id); return; }

    deleteSession(rec.sessionId, function (err) {
      if (err) {
        console.warn('[删除会话失败] ' + rec.sessionId, err);
        removeRecord(rec.id);   // 服务器上的删不掉也先隐藏，同时告诉用户原因
        appendMessage('bot', '（删除会话失败：' + err + '，刷新后可能会重新出现）');
        return;
      }
      console.log('[删除会话成功] ' + rec.sessionId);
      removeRecord(rec.id);
    });
  }

  // 删除记录：先弹窗二次确认（删除不可逆），用户点“确认删除”才走到 doDeleteRecord
  function deleteRecord(id) {
    var rec = findRecord(id);
    if (!rec) { return; }

    confirmDialog(
      '删除会话',
      '确定要删除这条会话吗？\n删除后服务器上的聊天记录会一起清除，且无法恢复。\n\n会话：' + (rec.sessionId || rec.name),
      function () { doDeleteRecord(rec); }
    );
  }

  /* ----------------------------- 事件绑定 ----------------------------- */
  // 注意别写成 .on('click', newGame)：那样会把 jQuery 的 Event 对象当成 pendingText 传进去
  $('#btnNewGame').on('click', function () { newGame(); });

  $('#recordList')
    .on('click', '.record', function () {
      switchRecord($(this).attr('data-id'));
    })
    .on('click', '.del', function (e) {
      e.stopPropagation();
      deleteRecord($(this).closest('.record').attr('data-id'));
    });

  $('#composer').on('submit', function (e) {
    e.preventDefault();
    console.log('[发送按钮] 触发 submit');
    var text = $.trim($('#answerInput').val());
    if (!text) { return; }
    $('#answerInput').val('');
    sendMessage(text);   // 调用 /api/chat，由后端判定并回复
  });

  // 点答题栏的小头像 = 让后端再出一道新题
  $('#answerRail').on('click', '.rail-avatar', function () {
    sendMessage('新题');
  });

  /* ----------------------------- 启动 ----------------------------- */
  // 把后端会话里的消息映射成前端聊天记录：role=user -> 我，role=assistant -> AI
  // role=system 是系统提示词，只在请求模型时带上，界面上不显示
  function fillMessages(rec, messages) {
    rec.messages = [];
    $.each(messages || [], function (_, m) {
      if (!m || typeof m.content !== 'string' || !m.content) { return; }
      if (m.role === 'user') { rec.messages.push({ who: 'me', text: m.content }); }
      else if (m.role === 'assistant') { rec.messages.push({ who: 'bot', text: m.content }); }
    });
    rec.loaded = true;
    return rec;
  }

  // 从后端读取某个会话的内容并渲染：历史会话点开时才调（懒加载）
  function loadSessionContent(rec) {
    console.log('[载入会话] ' + rec.sessionId);

    fetchSession(rec.sessionId, function (data, err) {
      fillMessages(rec, data && data.messages);
      renderRecords();
      renderMessages();

      if (err) {
        // 读取失败：不覆盖已有内容，只补一句提示，会话仍可继续用
        console.warn('[载入会话失败] ' + rec.sessionId, err);
        appendMessage('bot', '（读取该会话失败：' + err + '）');
        return;
      }

      // 会话是空的（建了但没聊过）：补个开场白并出第一道题
      if (!rec.messages.length) {
        appendMessage('bot', '你好呀！我是汉字谜盒的AI机器人，我们一起来猜字谜吧～');
        askRiddle();
      }
    });
  }

  // 首页启动流程：先查历史会话列表
  //   有历史   -> 列表里展示全部会话，自动打开第一条（最近的那条）
  //   没有历史 -> 走 newGame() 新建会话并出第一道题
  // 查询列表失败（后端没启动等）时同样退回新建，保证游戏还能玩
  function boot() {
    console.log('[启动] 查询历史会话列表…');

    fetchSessions(function (list, err) {
      if (err) {
        // 注意：newGame 的参数是“建好会话后要补发的消息”，不能把错误原因传进去
        console.warn('[启动] 会话列表查询失败，改为新建会话：', err);
        newGame();
        return;
      }

      if (!list.length) {
        console.log('[启动] 没有历史会话，新建一条');
        newGame();
        return;
      }

      // 全部历史会话都建一条记录放进列表（内容先不读，点开才加载）
      // 后端已按时间倒序返回，所以第一条就是最近一次会话
      records = [];
      $.each(list, function (_, sessionId) {
        createRecord(sessionId, sessionId);
      });
      currentId = records[0].id;

      console.log('[启动] 历史会话 ' + list.length + ' 条，默认打开最近一条：' + records[0].sessionId);
      renderRecords();
      renderMessages();

      // 只加载当前这一条；其余留到点击时再读，避免启动时一次性拉所有会话
      loadSessionContent(records[0]);
    });
  }

  // 用 try/catch 包住：一旦启动出错，控制台能看到，不至于“点了没反应又查不到原因”
  try {
    boot();
  } catch (e) {
    console.error('[启动异常]', e);
    appendMessage('bot', '（启动失败：' + (e && e.message ? e.message : e) + '）');
  }
});
