from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base_meta import Base

class Service(Base):
    __tablename__ = "Service"  #Устанавливается имя таблицы в базе данных, соответствующее данному классу

    # Определяются столбцы в таблице
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    doctor_id = Column(Integer, ForeignKey("Doctor.id")) #является внешним ключом, ссылается на столбец id таблицы Category.

    # Устанавливаются связи
    doctor = relationship("Doctor", back_populates="services")  # определяет отношение "многие(услуги) к одному(врачу)" между таблицами Doctor и Service.

    def __str__(self):
        return f"Service {self.id} {self.title} {self.price} {self.doctor_id}"

    def __repr__(self):
        return str(self)