from add import add

# "2,3,1" => 6

def test_2_3_1_should_be_6():
    # arrange
    expression = "2,3,1"
    expected = 6
    
    # act
    actual = add(expression)
    
    # assert
    assert expected == actual

def test_emptystring_should_be_error():
    # arrange
    expression = ""
    expected = -1
    
    # act
    actual = add(expression)
    
    # assert
    assert expected == actual
    
def test_wronginput_should_be_error():
    # arrange
    expression = "!,#"
    expected = -1
    
    # act
    actual = add(expression)
    
    # assert
    assert expected == actual

def test_wrongtype_should_be_error():
    # arrange
    expression = [2,4,[6234,512]]
    expected = -1
    
    # act
    actual = add(expression)
    
    # assert
    assert expected == actual

