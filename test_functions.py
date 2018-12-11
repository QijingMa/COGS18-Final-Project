"""Test for my functions."""

from functions import *

def test_Intro():
    
    
    Intro()
    assert True
    

def test_choosePokemon():
    choosePokemon()
    assert True
   

 def test_chooseSkill1():
        
        
        chooseSkill1()
        assert True
        
        
def test_chooseSkill2():
        
        chooseSkill2()
        assert True
        
        
def test_chooseSkill3():
        chooseSkill3()
        assert True  
    
    
def test_checkPath1():
    checkPath1(chosenSkill1)
    assert True
    
    
    
def test_checkPath2():
    checkPath2(chosenSkill2)
    assert True
    
    
    
def test_checkPath3():
    checkPath3(chosenSkill3)
    assert True
    
# Dont test functions that have user input
    


        
        
        
        
    
