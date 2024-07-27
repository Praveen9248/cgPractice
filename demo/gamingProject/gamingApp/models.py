from django.db import models
from django import forms

class PlayerModel(models.Model):
    player_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 10)

    def __str__(self):
        return self.player_name

class GameModel(models.Model):
    game_name = models.CharField(max_length = 20)
    score = models.IntegerField()
    players = models.ManyToManyField(PlayerModel)

    def __str__(self):
        return self.game_name

class PlayerForm(forms.ModelForm):
    class Meta:
        model = PlayerModel
        fields = "__all__"

class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = "__all__"