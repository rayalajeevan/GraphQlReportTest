from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    dob = Column(String)
    reports = relationship("Reports", back_populates="users")

class Course(Base):
    __tablename__ = 'course'
    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String)

class Tests(Base):
    __tablename__ = 'tests'
    test_id = Column(Integer(), primary_key=True, index=True)
    test_name = Column(String,nullable=False)
    reports = relationship("Reports", back_populates="tests")
 
class Reports(Base):
    __tablename__ = 'reports'
    report_id=Column(Integer(), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    test_id = Column(Integer, ForeignKey("tests.test_id"))
    report_percentage = Column(String)
    status= Column(String,nullable=False)
    tests = relationship("Tests", back_populates="reports")
    users = relationship("User", back_populates="reports")
    
    
    


    