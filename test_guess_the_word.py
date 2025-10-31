# Joseph Brekan
# CIS256
# EX 4

import builtins
import guess_the_word

# Ensure the random word chosen is from the predefined list
def test_selected_word_from_list(monkeypatch):

    word_list = ['sunflower', 'leather', 'monitor', 'tower', 'decoration', 'hunter']

    # Patch random.choice to return a known word
    monkeypatch.setattr('random.choice', lambda x: 'monitor')

    selected = guess_the_word.random.choice(word_list)
    assert selected in word_list


# Simulate a full game where all guesses are correct
def test_correct_guesses(monkeypatch, capsys):

    # Force the chosen word
    monkeypatch.setattr('random.choice', lambda x: 'dog')

    # Simulate user inputs for 'd', 'o', 'g'
    inputs = iter(['d', 'o', 'g'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    guess_the_word.word_guessing_game()

    # Capture printed output
    captured = capsys.readouterr().out

    # The output should contain success message
    assert 'Congratulations' in captured
    assert 'dog' in captured


# Simulate a game with all incorrect guesses leading to failure
def test_incorrect_guesses(monkeypatch, capsys):

    # Force the chosen word
    monkeypatch.setattr("random.choice", lambda x: "cat")

    # 6 wrong guesses (since 6 attempts are allowed)
    inputs = iter(["x", "y", "z", "q", "r", "s"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    guess_the_word.word_guessing_game()

    captured = capsys.readouterr().out

    # The output should contain the losing message
    assert "Out of attempts" in captured
    assert "cat" in captured


# Simulate a mix of correct and incorrect guesses
def test_mixed_correct_and_incorrect(monkeypatch, capsys):
    monkeypatch.setattr("random.choice", lambda x: "bug")

    # Mix of wrong and right guesses
    inputs = iter(["x", "b", "a", "u", "z", "g"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    guess_the_word.word_guessing_game()
    captured = capsys.readouterr().out

    # Should end with a win
    assert "Congratulations" in captured
    assert "bug" in captured

'''

Output:

PS C:\Users\joeyb\Desktop\School\Fall 2025\CIS256 (Python II)\Assignments\Module 4\CIS256_Joseph_Brekan_EX4> pytest -v 
======================================================================================================================== test session starts ========================================================================================================================
platform win32 -- Python 3.13.3, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\joeyb\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\joeyb\Desktop\School\Fall 2025\CIS256 (Python II)\Assignments\Module 4\CIS256_Joseph_Brekan_EX4
collected 4 items                                                                                                                                                                                                                                                     

test_guess_the_word.py::test_selected_word_from_list PASSED                                                                                                                                                                                                    [ 25%] 
test_guess_the_word.py::test_correct_guesses PASSED                                                                                                                                                                                                            [ 50%] 
test_guess_the_word.py::test_incorrect_guesses PASSED                                                                                                                                                                                                          [ 75%] 
test_guess_the_word.py::test_mixed_correct_and_incorrect PASSED  

'''