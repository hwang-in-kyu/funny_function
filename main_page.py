import streamlit as st

number = []

# or i in range(101) :
#     number.append(i)

# number -> 0, 1, 2, 3, 4, 5, ..., 100

st.title('릴스 시청 위험지수')

col1, col2= st.columns(2)

with col1 :
    reals = st.number_input('릴스 시청 개수 입력하세요 : ', min_value=0)
    st.write(reals)
    

with col2 :
    you = st.number_input('유튜브 시청 개수 입력하세요 : ',min_value=0)
    st.write(you)

sum_re_you = reals + you

st.button(sum_re_you)

if sum_re_you >= 100 :
    st.image('reals.png')
    
elif sum_re_you >= 80 :
    st.image('poison.jpg')

elif sum_re_you >= 60 :
    st.image('danger.jpg')
    
elif sum_re_you >= 40 :
    st.image('danger_close.jpg')

elif sum_re_you >= 20 :
    st.image('stop.jpg')

else :
    st.image('non_reals.png')