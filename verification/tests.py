init_code = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car'?")

Car = USER_GLOBAL['Car']

if not '__init__' in vars(Car):
    raise NotImplementedError("Where is '__init__' method?")

from inspect import signature

params = signature(Car.__init__).parameters
if not all((len(params) ==  3, 'self' in params, 'brand' in params, 'model' in params)):
    raise NotImplementedError("Check '__init__' arguments")

if not "some_car1" in USER_GLOBAL:
    raise NotImplementedError("Where is 'some_car1'?")

some_car1 = USER_GLOBAL['some_car1']

if not isinstance(some_car1, Car):
    raise TypeError("'some_car1' should be an instance of 'Car' class")

if not hasattr(some_car1, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'some_car1' object?")
    
if not isinstance(some_car1.brand, str):
    raise TypeError("'brand' attribute should be of type 'str'")

if not hasattr(some_car1, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'some_car1' object?")

if not isinstance(some_car1.model, str):
    raise TypeError("'model' attribute should be of type 'str'")

if not "some_car2" in USER_GLOBAL:
    raise NotImplementedError("Where is 'some_car2'?")

some_car2 = USER_GLOBAL['some_car2']

if not isinstance(some_car2, Car):
    raise TypeError("'some_car2' should be an instance of 'Car' class")

if not hasattr(some_car2, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'some_car2' object?")
    
if not isinstance(some_car2.brand, str):
    raise TypeError("'brand' attribute should be of type 'str'")

if not hasattr(some_car2, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'some_car2' object?")

if not isinstance(some_car2.model, str):
    raise TypeError("'model' attribute should be of type 'str'")

if not 'start_engine' in vars(Car):
    raise NotImplementedError("Where is 'start_engine' method?")

params2 = signature(Car.start_engine).parameters
if not all((len(params2) ==  1, 'self' in params2)):
    raise NotImplementedError("Check 'start_engine' arguments")
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "First": [
        prepare_test(middle_code='''''',
                     test="",
                     answer="")]}