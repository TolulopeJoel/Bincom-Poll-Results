from django.db import models


class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='state_name', max_length=50)

    class Meta:
        managed = False
        db_table = 'states'
        
    def __str__(self):
        return self.name
        

class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    name = models.CharField(db_column='lga_name', max_length=50)
    description = models.TextField(db_column='lga_description', blank=True, null=True)
    state = models.ForeignKey(State, related_name='states', null=True, on_delete=models.SET_NULL)

    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'lga'
        
    def __str__(self):
        return self.name



class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    name = models.CharField(db_column='ward_name', max_length=50)
    description = models.TextField(db_column='ward_description', blank=True, null=True)
    lga = models.ForeignKey(Lga, related_name='ward_lgas', on_delete=models.CASCADE)

    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ward'
        
    def __str__(self):
        return self.name


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    number = models.CharField(db_column='polling_unit_number', max_length=50, blank=True, null=True)
    name = models.CharField(db_column='polling_unit_name', max_length=50, blank=True, null=True)
    description = models.TextField(db_column='polling_unit_description', blank=True, null=True)
    uniquewardid = models.IntegerField(blank=True, null=True)
    ward = models.ForeignKey(Ward, related_name='wards', null=True, on_delete=models.SET_NULL)
    lga = models.ForeignKey(Lga, related_name='unit_lgas', null=True, on_delete=models.SET_NULL)

    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        ordering = ('-name',)
        db_table = 'polling_unit'
        
    def __str__(self):
        return self.name
        

class Party(models.Model):
    partyid = models.CharField(max_length=11)
    name = models.CharField(db_column='partyname', max_length=11)

    class Meta:
        managed = False
        db_table = 'party'
        
    def __str__(self):
        return self.name


class Agentname(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agentname'
        
    def __str__(self):
        return self.firstname + ' ' + self.lastname


class AnnouncedLgaResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'announced_lga_results'


class AnnouncedPuResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'announced_pu_results'


class AnnouncedStateResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'announced_state_results'


class AnnouncedWardResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'announced_ward_results'
