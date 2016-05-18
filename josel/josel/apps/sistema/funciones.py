from datetime import datetime
import datetime

from .models import Habitante



def anios(self):
	habitante = Habitante.objects.all()
	
	diff = datetime.date.today() - self.fecha_nac
	years = str(diff/365).split(' ')[0]
	return years