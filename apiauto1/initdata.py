from mysqlopertion import MySQLcaozuo
def inster_data(table, datas):
    db = MySQLcaozuo()
    db.clear(table)
    for data in datas:
        db.insert(table, data)
    db.select(table)
    db.close()

def select_data(table):
    db = MySQLcaozuo()
    db.select(table)
    db.close()

def update_data(table,key1,key2,value1,value2):
    db = MySQLcaozuo()
    db.update(table,key1,key2,value1,value2)
    db.close()

def update_data1(table,data1,data2):
    db = MySQLcaozuo()
    db.update1(table,data1,data2)
    db.close()

table_poll_question = "polls_question"
update_key2="question_text"
update_key1="id"
update_value1="1"
update_value2='"你喜欢的语言"'
update_2=['question_text','"你喜欢的语言"']
update_1=['id',"1"]
# update_poll_question=('id',1,'question_text','你喜欢哪种语言')
datas_poll_question =[{'id': 1, 'question_text': '你喜欢的游戏'}]
table_poll_choice = "polls_choice"
datas_poll_choice =[{'id': 1, 'choice_text': '生化危机', 'votes': 0, 'question_id': 1},
{'id': 2, 'choice_text': 'GTA5', 'votes': 0, 'question_id': 1}]

def init_data():
    inster_data(table_poll_question, datas_poll_question)
    inster_data(table_poll_choice, datas_poll_choice)
    update_data(table_poll_question,update_key1,update_key2,update_value1,update_value2)
    update_data1(table_poll_question,update_1,update_2)
    select_data(table_poll_question)
if __name__ == '__main__':
    init_data()

# print(inster_data(table_poll_question,datas_poll_question))
# inster_data(table_poll_question,datas_poll_question)