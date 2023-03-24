import pytest
from HW6.HW6_Task1 import words_sorting

def test_words_sorting_only_a_latter():
    words_lst = ["abb","aaa","a"]
    result = words_sorting(words_lst)
    assert result == ["a","aaa","abb"]

def test_words_sorting_upper_and_lower_case():
    words_lst = ["AAA","RRR","a","wWwW"]
    result = words_sorting(words_lst)
    assert result == ["a","aaa","rrr","wwww"]

def test_words_sorting_lst_in_lst():
    words_lst = ["aaa","sss",[],"bbb"]
    result = words_sorting(words_lst)
    assert result == ["aaa","bbb","sss"]

def test_words_sorting_int_in_lst():
    words_lst = ["aaa", "sss", 1, "bbb"]
    result = words_sorting(words_lst)
    assert result == ["aaa", "bbb", "sss"]

def test_words_sorting_none_in_lst():
    words_lst = ["aaa", "sss", None, "bbb"]
    result = words_sorting(words_lst)
    assert result == ["aaa", "bbb", "sss"]
def test_words_sorting_without_str():
    words_lst = [1.2, {}, 1]
    result = words_sorting(words_lst)
    assert result == []