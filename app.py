#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:45:28 2022

@author: max
"""

import streamlit as st
import datetime
from datetime import date

st.header("Ejemplo sencillo")

name = st.text_input("Nombres")
surname = st.text_input("Apellidos")
birth = st.date_input("Fecha de nacimiento", datetime.date(2000, 1, 1), min_value= datetime.date(1950, 1, 1))

def calculateAge(birthDate): 
    days_in_year = 365.2425    
    age = int((date.today() - birthDate).days / days_in_year) 
    return age 
          
edad = calculateAge(birth) 

st.write("Hola ", name, " ", surname)

st.write("Tu edad es  ", edad, " años")