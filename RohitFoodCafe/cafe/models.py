from django.db import models

class item(models.Model):
    id = models.AutoField(primary_key=True, name='id')
    item_name = models.CharField(max_length=100, name='item_name')
    item_type = models.CharField(max_length=50, name='item_type')
    description = models.TextField(max_length=500, name='description')
    cost = models.FloatField(name='cost')
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True, name='image')
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', name='status')

    def __str__(self):
        return str(self.id)+' , '+self.item_name+' , '+self.item_type+' , '+self.description+' , '+str(self.cost)+' , '+str(self.status)


class supplier(models.Model):
    id = models.AutoField(primary_key=True, name='id')
    person_name = models.CharField(max_length=100, name='person_name')
    shop_name = models.CharField(max_length=100, name='shop_name')
    location = models.CharField(max_length=100, name='location')
    phone_number = models.CharField(max_length=15, unique=True, name='phone_number')
    email = models.EmailField(max_length=100, unique=True, name='email')
    gst_number = models.CharField(max_length=15, unique=True, name='gst_number')
    specialized_in = models.CharField(max_length=100, name='specialized_in')
    specialized_items = models.TextField(max_length=500, name='specialized_items')
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', name='status')

    def __str__(self):
        return self.person_name+' , '+self.shop_name+' , '+self.location+' , '+self.phone_number+' , '+self.email+' , '+self.gst_number+' , '+self.specialized_in+' , '+self.specialized_items+' , '+str(self.status)  


class Role(models.Model):
    id = models.AutoField(primary_key=True, name='id')
    role_name = models.CharField(max_length=50, unique=True, name='role_name')
    role_description = models.TextField(max_length=500, name='role_description')
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', name='status')

    def __str__(self):
        return self.role_name+' , '+self.role_description+' , '+str(self.status)


class Employee(models.Model):
    id = models.AutoField(primary_key=True, name='id')
    employee_name = models.CharField(max_length=100, name='employee_name')
    email = models.EmailField(max_length=100, unique=True, name='email')
    phone_number = models.CharField(max_length=15, unique=True, name='phone_number')
    address = models.TextField(max_length=500, name='address')
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], name='gender')
    date_of_birth = models.DateField(name='date_of_birth')
    hire_date = models.DateField(name='hire_date')
    Role_id = models.ForeignKey(Role, on_delete=models.CASCADE, name='Role_id')
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', name='status')

    def __str__(self):
        return self.employee_name+' , '+self.email+' , '+self.phone_number+' , '+self.address+' , '+self.gender+' , '+str(self.date_of_birth)+' , '+str(self.hire_date)+' , '+str(self.Role_id)+' , '+str(self.status)


