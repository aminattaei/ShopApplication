from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse


class Food(models.Model):
    TYPE_FOOD = [
        ("lunch", "ناهار"),
        ("dinner", "شام"),
        ("drinks", "نوشیدنی"),
        ("dessert", "دسر"),
    ]

    title = models.CharField(_("نام غذا"), max_length=50)
    price = models.IntegerField(_("قیمت غذا"))
    content = models.TextField(_("توضیحات غذا"), null=True, blank=True)
    created_time = models.DateTimeField(
        _("زمان ایجاد غذا"), auto_now=False, auto_now_add=True
    )
    image = models.ImageField(_("تصویر غذا"), upload_to="foods/")

    Raw_materials = models.TextField(_("مواد اولیه"), null=True, blank=True)
    Nutritional_value = models.TextField(_("ارزش غذایی"), null=True, blank=True)
    food_type = models.CharField(
        _("دسته غذا"), max_length=50, choices=TYPE_FOOD, null=True, blank=True
    )

    class Meta:
        verbose_name = _("غذا")
        verbose_name_plural = _("غذاها")

    def __str__(self):
        return f"شماره غذا:{self.pk} - نام غذا : {self.title}"

    def get_absolute_url(self):
        return reverse("Food_detail", kwargs={"pk": self.pk})
