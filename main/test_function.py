# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 05:42:01 2021

@author: sijal

This is the test Module for the the Module/program function.py. This module 
help aware developer if there are any errors in the program function.py

pytest is the main libary that is used in this model to handle and the actions.
"""

# Importing the important Libaries
from function import ConnectionDatabaseError
from function import get_users_list_from_db
from function import connect_to_db
from function import TestDbError
from unittest import mock
from function import add

import pytest


# Testing the error/raise message.
@pytest.mark.parametrize(
    "db, error, msg",
    [
        ("test", TestDbError, "ERROR: YOU FORGOT TO MOCK connect_to_db"),
        ("te", ConnectionDatabaseError, "Can't connect to the databse!"),
    ],
)
def test_connect_to_db_errors(db, error, msg, capsys):
    """
    Use of parametize to minimize the coding.
    In this function funtion 'TestDbError' and 'ConnectionDatabaseError' are 
    detailedly checked. 
    * Check 1 if right exception is raised.
    * Check 2 based on the error, message printed is correct.
    * Check 3 does print output match with its correct database name.
    
    """
    with pytest.raises(error, match=msg):  # check error and messge generated match.
        connect_to_db(db)  # check error base on function.
    assert (
        capsys.readouterr().out == f"connection string:  {db}\n"
    )  # check the main print message.


# Testing the addition results.
def test_add():
    """
    Every possibility INT between 1 and 200 are tested to filter any minor errors.
    """
    for num_1 in range(1, 201):
        for num_2 in range(1, 201):
            for num_3 in range(1, 201):
                add_value = (
                    num_1 + num_2 + num_3
                )  # addition of every possbility of given intiger range
                assert add(num_1, num_2, num_3) == add_value

"""
# Testing output generated.
@mock.patch("function.connect_to_db")
def test_get_users_list_from_db(mock_connect_to_db):
    """
    * Normally connect_to_db() raise an error. so, mocke is used to handel this 
    issue.
    * json format list is created to similate database structure. for .get_user 
    to grab the user formats.
    """
    data = [
        {"username": "sijal", "birthday": "09/02/1994", "role": "admin"},
        {"username": "diky", "birthday": "06/08/1996", "role": "customer"},
        {"username": "raha", "birthday": "06/07/1964", "role": "manager"},
        {"username": "roma", "birthday": "19/09/1999", "role": "student"},
        {"username": "hulat", "birthday": "16/15/1979", "role": "Programmer"},
        {"username": "Dimak", "birthday": "17/08/1974", "role": "restro"},
        {"username": "Chaina", "birthday": "07/07/1970", "role": "Banker"},
        {"username": "Kai", "birthday": "05/05/1975", "role": "Guard"},
        {"username": "Pani", "birthday": "27/12/1990", "role": "Operator"},
        {"username": "Ako", "birthday": "15/05/1980", "role": "Sales"},
        {"username": "Jasto", "birthday": "05/08/1984", "role": "cook"},
        {"username": "Maan", "birthday": "05/08/1985", "role": "customer"},
        {"username": "Lagay", "birthday": "09/12/1965", "role": "Chef"},
        {"username": "Wosta", "birthday": "23/11/1991", "role": "Programmer"},
        {"username": "Lekhda", "birthday": "15/09/1987", "role": "Marketing"},
        {"username": "Huncha", "birthday": "23/11/1985", "role": "Waiter"},
        {"username": "Mind", "birthday": "11/12/1987", "role": "Sles"},
        {"username": "Nagari", "birthday": "26/05/1985", "role": "Operator"},
        {"username": "Lekhay", "birthday": "05/12/1990", "role": "Developer"},
        {"username": "Vaigo", "birthday": "12/12/1999", "role": "Designer"},
    ]


    for i in range(len(data)):
        test_parms = data[i]

        mock_connect_to_db.return_value = mock.Mock(
            **{"get_user.return_value": test_parms}
        )  # mock the connect_to_db fucntion  to ignore error and provid required data.

        assert get_users_list_from_db("test") == test_parms
if __name__ == __main__:
"""

# Testing output generated.
@mock.patch("function.connect_to_db")
def test_get_users_list_from_db(mock_connect_to_db):
    """
    * Normally connect_to_db() raise an error. so, mocke is used to handel this 
    issue.
    * json format list is created to similate database structure. for .get_user 
    to grab the user formats.
    """
    data = [
        {"username": "sijal", "birthday": "09/02/1994", "role": "admin"},
        {"username": "diky", "birthday": "06/08/1996", "role": "customer"},
        {"username": "raha", "birthday": "06/07/1964", "role": "manager"},
        {"username": "roma", "birthday": "19/09/1999", "role": "student"},
        {"username": "hulat", "birthday": "16/15/1979", "role": "Programmer"},
        {"username": "Dimak", "birthday": "17/08/1974", "role": "restro"},
        {"username": "Chaina", "birthday": "07/07/1970", "role": "Banker"},
        {"username": "Kai", "birthday": "05/05/1975", "role": "Guard"},
        {"username": "Pani", "birthday": "27/12/1990", "role": "Operator"},
        {"username": "Ako", "birthday": "15/05/1980", "role": "Sales"},
        {"username": "Jasto", "birthday": "05/08/1984", "role": "cook"},
        {"username": "Maan", "birthday": "05/08/1985", "role": "customer"},
        {"username": "Lagay", "birthday": "09/12/1965", "role": "Chef"},
        {"username": "Wosta", "birthday": "23/11/1991", "role": "Programmer"},
        {"username": "Lekhda", "birthday": "15/09/1987", "role": "Marketing"},
        {"username": "Huncha", "birthday": "23/11/1985", "role": "Waiter"},
        {"username": "Mind", "birthday": "11/12/1987", "role": "Sles"},
        {"username": "Nagari", "birthday": "26/05/1985", "role": "Operator"},
        {"username": "Lekhay", "birthday": "05/12/1990", "role": "Developer"},
        {"username": "Vaigo", "birthday": "12/12/1999", "role": "Designer"},
    ]

    mock_db = Mock()
    mock_db.return_value = data
    connection_string = mock_db

    for i in range(len(data)):
        test_parms = data[i]

        mock_connect_to_db.return_value = mock.Mock(
            **{"get_user.return_value": test_parms}
        )  # mock the connect_to_db fucntion  to ignore error and provid required data.

        assert get_users_list_from_db("test") == test_parms
if __name__ == __main__: