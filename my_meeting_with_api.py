from datetime import datetime
from copy import deepcopy
from fastapi import FastAPI
import uvicorn


app = FastAPI()

class MeetingScheduler:
    def __init__(self):
        self.__meeting_room_list = []
        self.__user_list = []
        self.__calendar = Calendar()

    def add_room(self, room):
        self.__meeting_room_list.append(room)

    def add_user(self, user):
        self.__user_list.append(user)

    def search_user(self, name):
        for u in self.__user_list:
            if u.name == name:
                return u

    def find_available_room(self, start_date, start_time, end_date, end_time, capacity):
        start_pdate = datetime.strptime(
            start_date + " " + start_time, '%d-%m-%Y %H:%M')
        end_pdate = datetime.strptime(
            end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_room = []
        for room in self.__meeting_room_list:
            if not room.is_available:
                continue
            if room.capacity < capacity:
                continue
            if not room.room_available(start_pdate, end_pdate):
                continue
            available_room.append(room)
        return available_room

    def book_room(self, subject, room_name, user_list, st_date, st_time, end_date, end_time):
        object_user_list = []
        for user in self.__user_list:
            if user.name in user_list:
                object_user_list.append(user)
        for room in self.__meeting_room_list:
            if room.id == room_name:
                meeting_room = room
                break
        interval = Interval(st_date, st_time, end_date, end_time)
        meeting_room.add_interval(interval)
        meeting = Meeting(subject, meeting_room, interval, object_user_list)
        self.__calendar.add_meeting(meeting)
        noti = Notification(meeting, meeting_room, interval)
        for user in object_user_list:
            user.add_notification(noti)
        return "success"

    def get_all_meeting_detail(self):
        meeting_list = []
        all_meeting = self.__calendar.meeting_list
        for meeting in all_meeting:
            meeting_list.append(meeting.__str__())
        return meeting_list

    def get__all_room_detail(self):
        room_list = []
        for room in self.__meeting_room_list:
            room_list.append(room.__str__())
        return room_list


class Calendar:
    def __init__(self):
        self.__meeting_list = []

    def add_meeting(self, meeting):
        self.__meeting_list.append(meeting)

    @property
    def meeting_list(self):
        return self.__meeting_list


class User:
    def __init__(self, name):
        self.__name = name
        self.__notification_list = []

    @property
    def name(self):
        return self.__name

    def add_notification(self, notification):
        self.__notification_list.append(deepcopy(notification))

    def get_unread_notification(self):
        noti_list = []
        for noti in self.__notification_list:
            if noti.read == None:
                noti_list.append(noti)
                noti.read = "Y"
        return noti_list

    def attend_meeting(self, meeting_subject_list):
        for noti in self.__notification_list:
            # print(noti.meeting.subject)
            # print(meeting_subject_list)
            if noti.meeting.subject in meeting_subject_list:
                noti.attend = 'Y'
                print("in loop")
                print(noti.meeting.subject)
                noti.meeting.add_user_attend(self)

    def show_all_notification(self):
        for noti in self.__notification_list:
            print(
                f"Meeting: {noti.meeting.subject} Room: {noti.room} read: {noti.read} attend: {noti.attend}")


class Notification:
    def __init__(self, Meeting, room, interval):
        self.__meeting = Meeting
        self.__room = room.id
        self.__start_time = interval.start_time
        self.__end_time = interval.end_time
        self.__read = None
        self.__attend = None

    @property
    def room(self):
        return self.__room

    @property
    def read(self):
        return self.__read

    @read.setter
    def read(self, value):
        self.__read = value

    @property
    def meeting(self):
        return self.__meeting

    @property
    def attend(self):
        return self.__attend

    @attend.setter
    def attend(self, attend):
        self.__attend = attend

    def __str__(self):
        return (f"Meeting Topics {self.__meeting.subject}")


class MeetingRoom:
    def __init__(self, id, capacity):
        self.__id = id
        self.__capacity = capacity
        self.__is_available = True
        self.__interval_list = []

    def is_available(self):
        return self.__is_available

    @property
    def id(self):
        return self.__id

    @property
    def capacity(self):
        return self.__capacity

    def add_interval(self, interval):
        self.__interval_list.append(interval)

    def check_no_overlap(self, start_time1, end_time1, start_time2, end_time2):
        if start_time1 > end_time2 or start_time2 > end_time1:
            return True
        else:
            return False

    def room_available(self, datetime1, datetime2):
        for i in self.__interval_list:
            if not self.check_no_overlap(i.start_time, i.end_time, datetime1, datetime2):
                return False
        return True

    def __str__(self):
        return (f"Room id : {self.__id} capacity {self.__capacity}")


class Interval:
    def __init__(self, start_date, start_time, end_date, end_time):
        self.__start_time = self.convert_str_datetime_to_datetime(
            start_date, start_time)
        self.__end_time = self.convert_str_datetime_to_datetime(
            end_date, end_time)

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return (self.__end_time)

    def __str__(self):
        return self.convert_datetime_to_str_datetime(self.__start_time)+" "+self.convert_datetime_to_str_datetime(self.__end_time)

    def convert_str_datetime_to_datetime(self, str_date, str_time):
        return datetime.strptime(str_date + " " + str_time, '%d-%m-%Y %H:%M')

    def convert_datetime_to_str_datetime(self, datetime):
        return datetime.strftime("%m/%d/%Y, %H:%M")


class Meeting:

    ID = 0

    def __init__(self, subject, meeting_room, interval, user_list):
        Meeting.ID += 1
        self.id = Meeting.ID
        self.__subject = subject
        self.__meeting_room = meeting_room
        self.__interval = interval
        self.__user_list = user_list
        self.__user_attend = []

    @property
    def subject(self):
        return self.__subject

    def add_user_attend(self, user):
        print(user.name)
        print(self.id)
        self.__user_attend.append(user)
        print(len(self.__user_attend))
        print(self.get_user_attend())
        return

    def get_user_attend(self):
        str = "user : "
        # print(len(self.__user_attend))
        for u in self.__user_attend:
            str = str + u.name + ","
        return str

    def __str__(self):
        m_str = "ID: " + str(self.id)
        m_str += " subject: " + self.__subject
        m_str += " Room: " + self.__meeting_room.id
        m_str += " Time : " + self.__interval.__str__()
        m_str += " User Attend: " + self.get_user_attend()
        print(self.get_user_attend())
        return m_str
        # return(f"subject: {self.__subject} Room: {self.__meeting_room.id} Time: {self.__interval.__str__()} User Attend: {self.get_user_attend()}")


def test_find_room_available():
    print("\nTest find room available")
    a_room = meet_system.find_available_room(
        "26-03-2023", "09:00", "26-03-2023", "16:00", 30)
    for i in a_room:
        print(i)


def test_room_booking():
    print("\nTest room booking")
    meet_system.book_room("OOP Study", "5", [
                          "john", "alice"], "26-03-2023", "09:00", "26-03-2023", "16:00")


meet_system = MeetingScheduler()
for i in range(10):
    room_id = i+1
    room_capacity = (i+1) * 10
    meet_system.add_room(MeetingRoom(str(room_id), room_capacity))


john = User("john")
meet_system.add_user(john)
meet_system.add_user(User("tom"))
meet_system.add_user(User("mary"))
meet_system.add_user(User("jenny"))
meet_system.add_user(User("bob"))
meet_system.add_user(User("alice"))

# test for use case find_room_available
#test_find_room_available()

# test for use case room booking and create meeting
#test_room_booking()

# show meeting
# print("\nShow all meeting")
# for i in meet_system.get_all_meeting_detail():
#     print(i)

# print for check room booked don't show again
# test_find_room_available()

# test for use case get notification of user
# print("\nGet unread notification")
# unread = john.get_unread_notification()
# for i in unread:
#     print(i)

# test user attend
# print("\nJoin meeting")
# john.attend_meeting(["OOP Study"])
# john.show_all_notification()

# show meeting
# for i in meet_system.get_all_meeting_detail():
#     print(i)


@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Ping": "Pong"}

# GET -- > Read Todo


@app.post("/get_available_room", tags=["book room"])
async def get_available_room(data: dict) -> dict:
    st_d = data["start_date"]
    st_t = data["start_time"]
    end_d = data["end_date"]
    end_t = data["end_time"]
    capacity = int(data["capacity"])
    a_room = meet_system.find_available_room(st_d, st_t, end_d, end_t, capacity)
    for i in a_room:
        print(i)
    dt = {}
    for i in a_room:
        dt[i.id] = i.capacity
    print(dt)
    return {"Data": dt}

@app.post("/book_room", tags=["book room"])
async def book_room(data: dict) -> dict:
    subject = data["subject"]
    room_id = data["room_id"]
    user_list = data["user"]
    st_d = data["start_date"]
    st_t = data["start_time"]
    end_d = data["end_date"]
    end_t = data["end_time"]
    status = meet_system.book_room(subject, room_id, user_list, st_d, st_t, end_d, end_t)
    return {"status": status}

@app.post("/unread_notification", tags=["notification"])
async def get_unread_notification(data: dict) -> dict:
    user = data["user"]
    object_user = meet_system.search_user(user)
    unread = object_user.get_unread_notification()
    ret = {}
    count = 1
    for noti in unread:
        temp = {}
        temp["meeting"] = noti.meeting.subject
        temp["room"] = noti.room
        ret[str(count)] = temp
        count += 1
    print(ret)
    return ret

if __name__ == "__main__":
    uvicorn.run("meeting_with_api:app", host="127.0.0.1", port=8000, log_level="info")
