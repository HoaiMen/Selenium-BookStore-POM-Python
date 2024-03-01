# -*- coding: utf8 -*- we should add test cases here because we can miss some cases while writing automation code or
# some manuel testers (test analystes) can handle this more efficiently we can obtain test cases from test management
#  tools, I used this for my previous project:
# http://www.inflectra.com/SpiraTest/Integrations/Unit-Test-Frameworks.aspx We can also record the result of test
# cases to test management tool

# for maintainability, we can seperate web test cases by page name but I just listed every case in same array


def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Test case 0', 'In Product page, when user click "Search", you will see Search List Page'],
    ['Test case 1', 'In Product page, when user click something category, you will see a list of products by category '],
    ['Test case 3', 'In Main page, when user click "Sign up" button, he should see Sign up Page'],
    ['Test case 2', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['Test case 4', 'In Main page, when user click "Sign in" button, he should see Sign in Page'],
    ['Test case 5', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
    ['Test case 6', 'In Main Page, when user click any product, he should see Detail Page'],
    ['Test case 7', 'In Detail Page, when user click "Add to cart", product should be add to cart,and he should see Cart Page'],
    ['Test case 8', 'In Main Page, when user click Icon cart, he should see Cart Page'],
    ['Test case 9', 'In Cart Page, when user click "Icon delete product", product should be deleted in cart'],
    ['Test case 10', 'In Main page, when user click Logo, the nain page will reload'],
]
