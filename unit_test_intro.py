import unittest
#each/every unit test runs independently of any other test even if same class

def sum(a,b):
    return a + b

class SumTest(unittest.TestCase):
    #Arrange - Arrange the method to run the test (initialize input values)
    def setUp(self):
        print("SETUP CALLED")
        self.a = 10
        self.b = 20
    
    def tearDown(self):
        self.a = 0
        self.b = 0
        print("TEARDOWN CALED")

    def test_sumfunc1(self):
        print("TEST 1 CALLED")
        #Act - Run the test (store the function in a result variable)
        result = sum(self.a,self.b)
        #Assert - Verify the test returns if it is successful or fail
        self.assertEqual(result, self.a + self.b)

    def test_sumfunc2(self):
        print("TEST 2 CALLED")
        #Act - Run the test (store the function in a result variable)
        result = sum(self.b,self.a)
        #Assert - Verify the test returns if it is successful or fail
        self.assertEqual(result, self.a + self.b)

class LearnTest(unittest.TestCase):
    #this doesnt work:
    def myfunc(self):
        pass

    #HAS to have "test_" in the test method name:
    def test_myfunc1(self):
        pass
    
    def test_function2(self):
        pass

    def test_function3(self):
        pass

#doesnt matter if code is in one class, or multiple classes
class AnotherTest(unittest.TestCase):
    #HAS to have "test_" in the test method name:
    def test_myfunc4(self):
        pass

    #can have same function name if used in different class:
    def test_function3(self):
        pass

#invoke the unittest framework (the main function of the unit test)
#will capture all the tests in the file or in imports and run them one by one
if __name__ == "__main__":
    unittest.main()