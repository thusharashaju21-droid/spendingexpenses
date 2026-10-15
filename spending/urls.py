from django.urls import path
from spending.views import SignUpView
from spending.views import GetMeView
from spending.views import ExpenseListCreateView
from spending.views import ExpenseRetrieveDeleteView
from spending.views import ExpenseSummaryView
from spending.views import BudgetPlanView

from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [

   path('register/',SignUpView.as_view()),
   path("me/",GetMeView.as_view()),
   path("expenses/",ExpenseListCreateView.as_view()),
   path("expenses/<int:pk>/",ExpenseRetrieveDeleteView.as_view()),
   path("expenses/summary/",ExpenseSummaryView.as_view()),
   path("expenses/budget/",BudgetPlanView.as_view()),

   path("token/",ObtainAuthToken.as_view()),

]