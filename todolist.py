from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

# Create database file
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# All model classes should inherit from the DeclarativeMeta class
Base = declarative_base()


class Table(Base):  # Create a model class that describes the table in the DB
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


# Create the table in the DB by generating SQL queries
Base.metadata.create_all(engine)


tasks = ["1) Today's tasks", "2) Week's tasks", "3) All tasks",
         '4) Missed tasks', '5) Add task', '6) Delete task', '0) Exit']
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]
response = 1

# Create a session to access the DB
Session = sessionmaker(bind=engine)
session = Session()

today_d = datetime.today()
today = str(today_d.day) + ' ' + today_d.strftime('%b')

while response != 0:
    [print(task) for task in tasks]  # Show menu
    response = int(input())
    print()
    if response == 1:
        print('Today', today + ":")     # Add date to print
        rows = session.query(Table).filter(Table.deadline == today_d.date()).all()
        if len(rows) == 0:
            print('Nothing to do!\n')
        else:
            for i in range(len(rows)):
                counter = 1
                n_row = rows[i]
                print(str(counter) + ".", n_row.task)
                counter += 1
            print()

    elif response == 2:
        for i in range(7):
            task_date = (today_d + timedelta(days=i)).date()
            rows = session.query(Table).filter(Table.deadline == task_date).all()
            print(days[task_date.weekday()], str(task_date.day) + ' ' + task_date.strftime('%b'))

            if len(rows) == 0:
                print('Nothing to do!\n')
            else:
                for q in range(len(rows)):
                    n_row = rows[q]
                    print(str(q + 1) + ".", n_row.task)
                    print()

    elif response == 3:
        rows = session.query(Table).order_by(Table.deadline).all()
        dates = []
        print("All tasks:")
        for i in range(len(rows)):
            n_row = rows[i]
            print(str(n_row.id) + ".", n_row.task + ".",
                  str(n_row.deadline.day) + ' '
                  + n_row.deadline.strftime('%b'))
        print()

    elif response == 4:
        rows = session.query(Table).filter(Table.deadline < today_d.date()).all()
        # rows = rows.order_by(Table.deadline)
        print("Missed tasks:")
        if len(rows) == 0:
            print("Nothing is missed!")
        else:
            for q in range(len(rows)):
                n_row = rows[q]
                print(str(q + 1) + ".", n_row.task + '.',
                      str(n_row.deadline.day) + ' '
                      + n_row.deadline.strftime('%b'))
        print()

    elif response == 5:
        task_name = input('Enter task\n')
        deadline_date = input('Enter deadline\n')
        # Create a new row, an object of the model class and pass it to add method
        new_row = Table(task=task_name,
                        deadline=datetime.strptime(deadline_date,
                                                   '%Y-%m-%d').date())
        session.add(new_row)
        session.commit()
        print('The task has been added!\n')

    elif response == 6:
        print("Choose the number of the task you want to delete:")
        rows = session.query(Table).order_by(Table.deadline).all()
        for i in range(len(rows)):
            n_row = rows[i]
            print(str(n_row.id) + ".", n_row.task + ".",
                  str(n_row.deadline.day) + ' '
                  + n_row.deadline.strftime('%b'))
        task_del = int(input())
        if len(rows) > 2:
            specific_row = rows[task_del + 1]
            session.delete(specific_row)
            session.commit()
        print("The task has been deleted!")
        print()

    else:
        print('Bye!')
