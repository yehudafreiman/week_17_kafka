from fastapi import APIRouter
from dal import get_top_customers, get_customers_without_orders, get_zero_credit_active_customers

router = APIRouter()

@router.get("/analytics/top-customers")
def top_customers():
    return get_top_customers()

@router.get("/analytics/customers-without-orders")
def customers_without_orders():
    return get_customers_without_orders()

@router.get("/analytics/zero-credit-active-customers")
def zero_credit_active_customers():
    return get_zero_credit_active_customers()