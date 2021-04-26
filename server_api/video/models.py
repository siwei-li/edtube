from django.db import models

class Video(models.Model):
    VIDEO_SOURCES=[('YT','youtube'),
                   ('KA','khanacademy')]

    source = models.CharField(max_length=2,
                              choices=VIDEO_SOURCES,
                              default='YT')
    platform_id = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    # If you specify a max_length attribute,
    # it will be reflected in the Textarea widget of the auto-generated form field.
    # However it is not enforced at the model or database level.
    description = models.TextField(max_length=5000)
    pub_date = models.DateTimeField('Date Published')
    # db_index=True
    category_id = models.IntegerField()
    channel_id = models.CharField(max_length=50,blank=True)
    channel_title = models.CharField(max_length=100,blank=True)

    class Meta:
        db_table = 'videos'  # 指明数据库表名

    def __str__(self):
        return "Video " + str(self.id) + "@"+self.source + "#" + str(self.platform_id)

