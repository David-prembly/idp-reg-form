from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200)
    venue = models.TextField(null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True)
    attendees = models.IntegerField(default=0)


class Exhibitor(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, related_name='event')
    name = models.CharField(max_length=200)
    booth = models.CharField(max_length=20, null=True, blank=True)
    leads = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class Leads(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True, related_name='event')
    exhibitor = models.ForeignKey(Exhibitor, on_delete=models.SET_NULL, null=True, related_name='exhibitors')
    fullName = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    mobileNumber = models.CharField(max_length=20, null=True, blank=True)
    registrationType = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=30, null=True, blank=True)
    role = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return self.fullName

    @property
    def exhibitor_name(self):
        return self.exhibitor.name


class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True, related_name='event')
    fullName = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    mobileNumber = models.CharField(max_length=20, null=True, blank=True)
    registrationType = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=30, null=True, blank=True)
    role = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.fullName
