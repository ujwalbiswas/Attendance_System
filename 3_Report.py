import streamlit as st
import Face_rec

st.set_page_config(page_title='Reporting',layout='wide')

st.subheader('Reporting')

# show the logs data 
# extract data 
name = 'attendance:logs'
def load_logs(name,end=-1):
    logs_list = Face_rec.r.lrange(name,start=0,end=end)
    return logs_list

# tabs to show infoo
tab1, tab2 = st.tabs(['Ragistered Data','Logs'])


with tab1:
    if st.button('Refresh Data'):
    #retrive data from radis
# Retrive the data fro Radis Database
        with st.spinner('Retriving Data from Redis DB ...'):
         redis_face_db = Face_rec.retrive_data(name='academy:register')
         st.dataframe(redis_face_db[['Name','Role']]) 
with tab2:
    if st.button('Refresh Logs'):
        st.write(load_logs(name=name))
    

