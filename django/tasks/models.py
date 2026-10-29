from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "Por hacer"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        DONE = "DONE", "Completada"

    # ForeignKey: cada Task pertenece a UN Project.
    # Un Project puede tener MUCHAS Task — relación muchos a uno.
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}"

class Motocicleta(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cilindrada = models.CharField(max_length=50)
    precio = models.CharField(max_length=50) 
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.marca} {self.modelo}"









#De uno a no uno
class Sensei(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)


#uno a muchos
class Alumno(models.Model):
    sensei=models.ForeignKey(
        Sensei, on_delete=models.CASCADE, 
        related_name='alumnos')
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    misiones = models.ManyToManyField('Mision', related_name='alumnos')
    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pefiles/')


class Mision(models.Model):
   
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)   
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    titulo = models.CharField(max_length=100)
    objetivo = models.TextField(blank=True)

    estudiantes= models.ManyToManyField(
        Estudiantes, 
        through='Participacion')

class Participacion(models.Model):
    estudiante = models.ForeignKey(
        Estudiantes,
        on_delete=models.CASCADE)
    actividad = models.ForeignKey(
        Actividad, 
        on_delete=models.CASCADE)
    rol=models.CharField(max_length=50) 
    created_at = models.DateTimeField(auto_now_add=True)    






#Desde aqui clase 29-10-2026

