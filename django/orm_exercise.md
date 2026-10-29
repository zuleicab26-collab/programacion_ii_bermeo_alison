Motocicleta.objects.all()
<QuerySet [<Motocicleta: susuki sm-9>]>

>>> Motocicleta.objects.create(
... marca="vespa",
... modelo="vespa VXL 150",
... cilindrada="150cc",
... precio="3.955"
... )
<Motocicleta: vespa vespa VXL 150>


>>> moto=Motocicleta(marca="Yamaha", modelo="XTZ 125E", cilindrada="125cc", precio="3.599")
<bound method Model.save of <Motocicleta: Yamaha XTZ 125E>>
>>> moto.save()


>>> Motocicleta.objects.get(marca="Yamaha")
<Motocicleta: Yamaha XTZ 125E>
>>> 


>>> Motocicleta.objects.get(pk=2)
<Motocicleta: vespa vespa VXL 150>


>>> Motocicleta.objects.filter(marca="Yamaha")
<QuerySet [<Motocicleta: Yamaha XTZ 125E>]>


Motocicleta.objects.exclude(marca="Yamaha")
<QuerySet [<Motocicleta: susuki sm-9>, <Motocicleta: vespa vespa VXL 150>]>


>>> Motocicleta.objects.filter(marca="Yamaha")
<QuerySet [<Motocicleta: Yamaha XTZ 125E>]>


>>> Motocicleta.objects.filter(marca__contains="Yamaha")
<QuerySet [<Motocicleta: Yamaha XTZ 125E>]>


>>> Motocicleta.objects.filter(marca__icontains="YAMAHA")
<QuerySet [<Motocicleta: Yamaha XTZ 125E>]>


>>> Motocicleta.objects.filter(marca__startswith="Yamaha")
<QuerySet [<Motocicleta: Yamaha XTZ 125E>]>


>>> from datetime import date
>>> Motocicleta.objects.filter(created_at__gte=date(2026, 1, 1))
/home/alumnos/Documents/programacion_ii_bermeo_alison/django/venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1653: RuntimeWarning: DateTimeField Motocicleta.created_at received a naive datetime (2026-01-01 00:00:00) while time zone support is active.
  warnings.warn(
<QuerySet [<Motocicleta: susuki sm-9>, <Motocicleta: vespa vespa VXL 150>, <Motocicleta: Yamaha XTZ 125E>]>
>>> 


>>> Motocicleta.objects.filter(marca__isnull=True)
<QuerySet []>


>>> Motocicleta.objects.filter(marca__in=["Yamaha", "Migración ERP"])
<QuerySet [<Motocicleta: Yamaha XTZ 125E>]>


>>> Motocicleta.objects.filter(modelo__icontains="a", created_at__gte=date(2026, 1, 1))
/home/alumnos/Documents/programacion_ii_bermeo_alison/django/venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1653: RuntimeWarning: DateTimeField Motocicleta.created_at received a naive datetime (2026-01-01 00:00:00) while time zone support is active.
  warnings.warn(
<QuerySet [<Motocicleta: vespa vespa VXL 150>]>


>>> Motocicleta.objects.order_by("cilindrada")
<QuerySet [<Motocicleta: Yamaha XTZ 125E>, <Motocicleta: vespa vespa VXL 150>, <Motocicleta: susuki sm-9>]>


>>> Motocicleta.objects.order_by("-created_at")
<QuerySet [<Motocicleta: Yamaha XTZ 125E>, <Motocicleta: vespa vespa VXL 150>, <Motocicleta: susuki sm-9>]>


>>> Motocicleta.objects.order_by("modelo", "-created_at")
<QuerySet [<Motocicleta: susuki sm-9>, <Motocicleta: vespa vespa VXL 150>, <Motocicleta: Yamaha XTZ 125E>]>


>>> Motocicleta.objects.count()
3


>>> Motocicleta.objects.filter(marca__icontains="Yamaha").count()
1


>>> Motocicleta.objects.filter(modelo="No existe").exists()
False


>>> Motocicleta.objects.exists()
True


>>> queryset = Motocicleta.objects.filter(modelo__icontains="a")
>>> queryset = queryset.exclude(modelo="XTZ 125E")
>>> queryset = queryset.order_by("-created_at")
>>> print(queryset.query)
SELECT "tasks_motocicleta"."id", "tasks_motocicleta"."marca", "tasks_motocicleta"."modelo", "tasks_motocicleta"."cilindrada", "tasks_motocicleta"."precio", "tasks_motocicleta"."created_at" FROM "tasks_motocicleta" WHERE (UPPER("tasks_motocicleta"."modelo"::text) LIKE UPPER(%a%) AND NOT ("tasks_motocicleta"."modelo" = XTZ 125E)) ORDER BY "tasks_motocicleta"."created_at" DESC



