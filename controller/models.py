from django.db import models
from components.models import component
# Create your models here.

class components_provided(models.Model):
    FIRST_YEAR='1st YEAR'
    SECOND_YEAR='2nd YEAR'
    THIRD_YEAR='3rd YEAR'
    FOURTH_YEAR='4th YEAR'
    choice_year=(
        (FIRST_YEAR,'First year'),
        (SECOND_YEAR,'Second year'),
        (THIRD_YEAR,'Third year'),
        (FOURTH_YEAR,'Fourth year'),
    )
    choice_section=(
        ('ECE A','ECE A'),
        ('ECE B','ECE B'),
        ('ECE C','ECE C'),
    )
    detail=models.ForeignKey(component)
    quantity=models.IntegerField(default=1)
    student_name=models.CharField(max_length=100,null=False)
    roll_number=models.CharField(max_length=100,null=False)
    section=models.CharField(max_length=100,choices=choice_section,null=False)
    year=models.CharField(max_length=100,choices=choice_year,null=False)
    mobile=models.BigIntegerField(null=False)
    email_id=models.EmailField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date=models.DateField(null=True)
    deleted_at = models.DateTimeField(null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.detail.name

    def clean(self):
        self.student_name=self.student_name.upper()
        self.roll_number=self.roll_number.upper()