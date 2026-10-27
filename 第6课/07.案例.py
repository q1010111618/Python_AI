"""
某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。系统中有两种类型的会员：
普通会员和VIP会员，他们的结束权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。
核心功能：
1.会员登录：会员通过卡号和密码登录系统
2.借书：会员可以借阅库存中有余量的图书
3.还书：会员可以归还借阅的图书
4.查看我的借阅：展示当前会员已经借阅的图书列表
5.退出系统
借阅规则：
1.普通会员最多只能借阅3本图书
2.VIP会员最多可借6+VIP等级本（VIP等级，默认为1）
注意：
1.登录成功（卡号密码均正确）后，才可以访问系统
2.图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书
"""


class Book:
    """图书：只负责维护自己的馆藏数量与可借余量"""

    def __init__(self, book_id, name, author, total):
        self.book_id: str = book_id      # 图书编号
        self.name: str = name            # 书名
        self.author: str = author         # 作者
        self.total: int = total           # 馆藏总数
        self.stock: int = total           # 当前可借余量

    def borrow_one(self):
        """借出 1 本，成功返回 True，库存不足返回 False"""
        if self.stock <= 0:
            return False
        self.stock -= 1
        return True

    def return_one(self):
        """归还 1 本，成功返回 True，数量已超馆藏（异常数据）返回 False"""
        if self.stock >= self.total:
            return False
        self.stock += 1
        return True

    def __str__(self):
        return f"[{self.book_id}]《{self.name}》 作者:{self.author}  可借：{self.stock} 总数：{self.total}"


class Member:
    """会员基类：封装登录与借还书的通用逻辑，最大借阅量由子类决定"""

    def __init__(self, card_no, password, name):
        self.card_no: str = card_no
        self.name: str = name
        self.__password: str = password      # 私有属性：密码不允许外部直接读写
        self.__borrowed: list[Book] = []     # 私有属性：借阅清单只能通过 borrow_book/return_book 修改

    def login(self, card_no, password):
        if self.card_no == card_no and self.__password == password:
            return True
        else:
            return False

    @property
    def borrowed(self) -> list[Book]:
        """只读访问已借图书：返回副本，避免外部绕过借还逻辑直接改列表"""
        return self.__borrowed.copy()

    @property
    def borrowed_count(self) -> int:
        return len(self.__borrowed)

    @property
    def max_borrow(self) -> int:
        """最大可借数量（基类按普通会员处理，子类可重写）"""
        return 3

    def borrow_book(self, book):
        """借书，返回 (是否成功, 提示信息)"""
        if self.borrowed_count >= self.max_borrow:
            return False, f"借书失败：最多只能借 {self.max_borrow} 本，请先归还部分图书"
        if book in self.__borrowed:
            return False, f"借书失败：你已经借过《{book.name}》，不能重复借阅"
        if not book.borrow_one():
            return False, f"借书失败：《{book.name}》库存不足"
        self.__borrowed.append(book)
        return True, f"借书成功：《{book.name}》（已借 {self.borrowed_count}/{self.max_borrow} 本）"

    def return_book(self, book):
        """还书，返回 (是否成功, 提示信息)"""
        if book not in self.__borrowed:
            return False, f"还书失败：你没有借阅《{book.name}》"
        if not book.return_one():
            return False, f"还书失败：《{book.name}》库存数据异常"
        self.__borrowed.remove(book)
        return True, f"还书成功：《{book.name}》（已借 {self.borrowed_count}/{self.max_borrow} 本）"

    def __str__(self):
        return f"{self.name}（卡号 {self.card_no}）"


class NormalVIP(Member):
    """普通会员：最多借 3 本，没有 VIP 等级（直接复用基类的 __init__）"""

    @property
    def max_borrow(self):
        return 3


class VIP(Member):
    """VIP会员：最多借 6 + VIP等级 本，level 只有 VIP 才有"""

    def __init__(self, card_no, password, name, level=1):
        super().__init__(card_no, password, name)
        self.level: int = level   # VIP等级，默认为 1

    @property
    def max_borrow(self):
        return 6 + self.level


class Library:
    """图书馆：管理全部图书与会员，负责查询和登录校验"""

    def __init__(self, books, members):
        self.books: list[Book] = books
        self.members: list[Member] = members

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, card_no):
        for member in self.members:
            if member.card_no == card_no:
                return member
        return None

    def login(self, card_no, password):
        """卡号与密码均正确才返回会员对象，否则返回 None"""
        member = self.find_member(card_no)
        if member and member.login(card_no, password):
            return member
        return None

    def available_books(self):
        return [book for book in self.books if book.stock > 0]


def print_books(books, title="图书列表"):
    print(f"\n===== {title} =====")
    if not books:
        print("（暂无图书）")
        return
    for book in books:
        print(book)
    print("==================")


def show_menu(current_member):
    print("\n========== 社区图书馆管理系统 ==========")
    print(f"当前会员：{current_member.name}  已借 {current_member.borrowed_count}/{current_member.max_borrow} 本")
    print("1.切换账号    2.借书    3.还书    4.查看我的借阅    5.退出系统")
    print("========================================")


def login_first(library):
    """进入系统前必须先登录：失败可反复重试，输入 q 退出程序"""
    print("\n========== 社区图书馆管理系统 ==========")
    print("请先登录后再使用系统（输入 q 退出程序）")
    print("========================================")

    while True:
        card_no = input("请输入卡号：").strip()
        if card_no.lower() == "q":
            return None
        password = input("请输入密码：").strip()

        member = library.login(card_no, password)
        if member:
            print(f"\n登录成功，欢迎 {member.name}！最多可借 {member.max_borrow} 本")
            return member
        print("登录失败：卡号或密码不正确，请重新输入")


def do_borrow(library, member):
    print_books(library.available_books(), "可借阅图书")
    book_id: str = input("请输入要借阅的图书编号（直接回车返回菜单）：").strip()
    if not book_id:
        return
    book = library.find_book(book_id)
    if book is None:
        print(f"借书失败：不存在编号为 {book_id} 的图书")
        return
    _, msg = member.borrow_book(book)
    print(msg)


def do_return(member):
    if not member.borrowed:
        print("你当前没有借阅任何图书")
        return
    print_books(member.borrowed, "我的借阅")
    book_id = input("请输入要归还的图书编号（直接回车返回菜单）：").strip()
    if not book_id:
        return
    target = None
    for book in member.borrowed:
        if book.book_id == book_id:
            target = book
            break
    if target is None:
        print(f"还书失败：你没有借阅编号为 {book_id} 的图书")
        return
    _, msg = member.return_book(target)
    print(msg)


def show_borrowed(member):
    if not member.borrowed:
        print("\n你当前没有借阅任何图书")
        return
    print_books(member.borrowed, f"{member.name} 的借阅列表")
    print(f"共 {len(member.borrowed)} 本，最多可借 {member.max_borrow} 本")


def build_library():
    """初始化演示数据"""
    books = [
        Book("B001", "Python编程：从入门到实践", "Eric Matthes", 3),
        Book("B002", "流畅的Python", "Luciano Ramalho", 2),
        Book("B003", "深入理解计算机系统", "Randal Bryant", 2),
        Book("B004", "三体", "刘慈欣", 5),
        Book("B005", "活着", "余华", 4),
    ]
    members = [
        NormalVIP("N1001", "123456", "张三"),
        VIP("V2001", "123456", "李四", level=2),   # 最多借 8 本
        VIP("V2002", "123456", "王五", level=3),   # 最多借 9 本
    ]
    return Library(books, members)


def show_unreturned(member):
    """列出当前会员未归还的图书"""
    if not member.borrowed_count:
        return
    print(f"\n{member.name} 还有 {member.borrowed_count} 本图书未归还：")
    for book in member.borrowed:
        print("  -", book.name)


def run_menu(library, member):
    """登录成功后的业务菜单：返回 True 表示切换账号，返回 False 表示退出系统"""
    while True:
        show_menu(member)
        choice = input("请选择功能（1-5）：").strip()

        if choice == "1":
            # 退出登录：只清掉当前登录态，借阅数据与库存保留，回到登录界面
            show_unreturned(member)
            print(f"\n{member.name} 已退出登录，请重新登录")
            return True

        elif choice == "2":
            do_borrow(library, member)
        elif choice == "3":
            do_return(member)
        elif choice == "4":
            show_borrowed(member)

        elif choice == "5":
            show_unreturned(member)
            print("\n已退出系统，欢迎下次光临！")
            return False

        else:
            print("输入无效，请输入 1-5 之间的数字")


def main():
    library = build_library()

    while True:
        # 1. 先登录，登录成功前不显示任何业务菜单
        member = login_first(library)
        if member is None:
            print("已退出系统，欢迎下次光临！")
            return

        # 2. 进入业务菜单：选“切换账号”会回到登录界面，选“退出系统”则结束程序
        if not run_menu(library, member):
            return


if __name__ == "__main__":
    main()
