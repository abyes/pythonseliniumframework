#fixtures are basically a method in which u define pre requsite or post requsite
#like if you want to run one command opening a browser so you can define that in fixtures and it can be uses in all places
#we can define fixrures in congftest file so it will be shared with all file and we can use it whereever we want
import pytest

@pytest.mark.usefixtures #(setup) # for example i define fixture in my confgtest file so to intialize this method
#on this calss i will define fixture like this
#and on cofgtest file if i define scope = class so it will run only first time
#when u define fixture gloabally so u dont need to define it to other methods but the only time when u required
#is when u are returning something from ur fixture
@pytest.fixture()
def fixture():
    print("i will be running first ")
    yield #this is to know python that it will be

def test_fixture2(fixture):
    print("after first it will run because it have value of first method ")
