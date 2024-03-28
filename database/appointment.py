from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base_meta import Base

class Appointment(Base):
    __tablename__ = "Appointment"  #Устанавливается имя таблицы в базе данных, соответствующее данному классу

    # Определяются столбцы в таблице
    office_number = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, ForeignKey("Doctor.id")) #является внешним ключом, ссылается на столбец id таблицы доктор
    patient_id = Column(Integer, ForeignKey("Patient.id"))
    date_and_time = Column(String(20), nullable=False)

    # Устанавливаются связи
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")

    def __str__(self):
        return f"Service {self.office_number} {self.doctor_id} {self.patient_id} {self.date_and_time}"

    def __repr__(self):
        return str(self)