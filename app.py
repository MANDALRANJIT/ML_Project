import streamlit as st
import pickle
st.title("MPG ML Project")
#displacement = st.number_input('enter a value for displacement')
displacement = st.number_input('Displacement', value = 300, placeholder='enter a value for displacement')
horsepower = st.number_input('Horsepower', value = 130, placeholder='enter a value for horsepower')
weight = st.number_input('Weight', value = 3000, placeholder='enter a value for weight')
acceleration = st.number_input('Acceleration', value = 10, placeholder='enter a value for acceleration')
st.write(displacement,horsepower,weight,acceleration)
loadedmodel = pickle.load(open('mpg_regression_model.sav','rb'))
prediction=loadedmodel.predict([[displacement,horsepower,weight,acceleration]])
st.subheader(f'predicted mpg value for the above parameters is {round(prediction[0], 2)}')
#st.write(prediction)
