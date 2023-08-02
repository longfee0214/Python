"""
重复执行N遍某函数
装饰器
"""


def repeat_test(num):
    def repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                try:
                    func(*args, **kwargs)
                except AssertionError as e:
                    print(f"Test failed with {str(e)}")
                    raise e
        
        return wrapper
    
    return repeat


@repeat_test(5)
def do_task():
    print("aaa")
    assert True
    
    assert False


if __name__ == "__main__":
    do_task()
    