from django.contrib import admin

from .models import (
    OrderRegistrationCase,
    Custom,
    EntranceEdg,
    ShippingType,
    Incoterms,
    MainData,
    Currency,
    CustomsAndShipping,
    Bank,
    BankBranch, CurrencySupply,
    Financial,
    ManufactureYear,
    Packing,
    Ware,
    # Documents,

)


@admin.register(OrderRegistrationCase)
class OrderRegistrationCaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Custom)
class CustomAdming(admin.ModelAdmin):
    pass


@admin.register(EntranceEdg)
class EntranceEdgAdming(admin.ModelAdmin):
    pass


@admin.register(ShippingType)
class ShippingTypeAdming(admin.ModelAdmin):
    pass


@admin.register(Incoterms)
class IncotermsAdming(admin.ModelAdmin):
    pass


@admin.register(MainData)
class MainDataAdming(admin.ModelAdmin):
    pass


@admin.register(Currency)
class CurrencyAdming(admin.ModelAdmin):
    pass


@admin.register(CustomsAndShipping)
class CustomsAndShippingAdming(admin.ModelAdmin):
    pass


@admin.register(Bank)
class BankAdming(admin.ModelAdmin):
    pass


@admin.register(BankBranch)
class BankBranch(admin.ModelAdmin):
    pass


@admin.register(CurrencySupply)
class CurrencySupplyAdming(admin.ModelAdmin):
    pass


@admin.register(Financial)
class FinancialAdming(admin.ModelAdmin):
    pass


@admin.register(ManufactureYear)
class ManufactureYearAdming(admin.ModelAdmin):
    pass


@admin.register(Packing)
class PackingAdming(admin.ModelAdmin):
    pass


@admin.register(Ware)
class WareAdming(admin.ModelAdmin):
    pass


# @admin.register(Documents)
# class DocumentsAdming(admin.ModelAdmin):
#     pass
