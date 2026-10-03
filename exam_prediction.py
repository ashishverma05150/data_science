import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import mysql.connector
st.title("student performance prediction")
st.write("### multiple linear regression using streamlit")
st.divider()
b1=st.checkbox("show database")
df= pd.read_csv(r"C:\Users\Abhishek Verma\Downloads\linear_regression_student_performance_1000_scaled (1).csv")
df1=df.head()
if b1:
    st.dataframe(df1)
s1 , s2 , s3 = st.columns(3)
s1.metric("total no. of  rows ", df.shape[0])
s3.metric("total no. of null values", df.isnull().sum().sum())
s2.metric("total no. of columns", df.shape[1])
X=df[["study_hours", "sleep_hours" ,"attendance" ,"previous_score" ,"practice_tests", "assignment_score"]]
y=df[["exam_score"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression()
s4, s5= st.columns(2)
s4.number_input("Enter the hours of study", min_value=0.0, max_value=10.0, step=0.01, key="hours")
s5.number_input("Enter the Attendence" ,  min_value=0.0, max_value=10.0, step=0.01)
s6, s7= st.columns(2)
s6.number_input("Enter the asignment_score", min_value=0.0, max_value=10.0, step=0.01)
s7.number_input("Enter the previous_score", min_value=0.0, max_value=10.0, step=0.01)
s8, s9= st.columns(2)
s8.number_input("Enter the practise_test", min_value=0.0, max_value=10.0, step=0.01)
s9.number_input("Enter the exam score", min_value=0.0, max_value=10.0, step=0.01)
c1,c2,c3,c4,c5= st.columns(5)
b2= c3.button("Analyse the value")
lr.fit(X_train, y_train)
prediction= lr.predict(X_train)
if b2:
    #Ye line prediction ke andar se actual predicted number nikalti hai.
    score = prediction[0][0]
    #buss yhh point hai ki jo bhi humne yaad krna hai 
    st.success(f"Predicted Exam Score: {score:.2f}")
    #Yahan .2f ka matlab hai: decimal point ke baad sirf 2 digits dikhana.
    if score >= 0.33:
         st.success("Result: PASS")
    else:
        st.error("Result: FAIL")
db=mysql.connector.connect(
    host="localhost"
    user="root"
    database="exam_prediction"
    passwaord="@Ashish99688"
)
cursor = db.cursor()
 query = """
            INSERT INTO exam_prediction
            (
               study_hours ,
               sleep_hours,
               attendance,
               previous_score,
               practice_tests,
               assignment_score,
               exam_score,

            )
            VALUES
            (
                %s, %s, %s, %s, %s, %s, %s
            )
            """

            values = (
                study_hours ,
               sleep_hours,
               attendance,
               previous_score,
               practice_tests,
               assignment_score,
               exam_score,

            )

            cursor.execute(query, values)

            db.commit()