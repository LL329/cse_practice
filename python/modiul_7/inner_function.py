def double_decker():
    print('Starting the double ducker')
    def inner_fun():
        print('inside the inner')
        return 5000
    return inner_fun

# print(double_decker()())
def do_something(work):
    print('work started')
    work()
    print('work ended')


# do_something(2)
# do_something('i am busy now')
def coding():
    print('coding in python')

do_something(coding)
