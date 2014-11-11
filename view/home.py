import web
import forms
from model.task import SnailTask, QuailTask
from model.user_repository import UserRepository, MongoWrapper, UserFactory


class Home:
    def __init__(self):
        self.snail_task_form = forms.SnailTaskForm().form
        self.quail_task_form = forms.QuailTaskForm().form
        self.watermelon_task_form = forms.WatermelonTaskForm().form
        self.reward_form = forms.RewardForm().form
        self.complete_task_form = forms.CompleteTaskForm().form
        self.purchase_reward_form = forms.PurchaseRewardForm().form
        self.delete_task_form = forms.DeleteTaskForm().form
        self.delete_reward_form = forms.DeleteRewardForm().form
        self.habit_form = forms.HabitForm().form
        self.complete_habit_form = forms.CompleteHabitForm().form
        self.render = web.template.render('templates',
                                          globals={'is_snail': is_snail,
                                                   'is_quail': is_quail})

    def render_home_page(self, user, error=None):
        return self.render.home(error,
                                user.purse.todays_total,
                                user.purse.total,
                                user.rewards,
                                user.tasks,
                                user.habits,
                                self.reward_form,
                                self.snail_task_form,
                                self.quail_task_form,
                                self.watermelon_task_form,
                                self.complete_task_form,
                                self.purchase_reward_form,
                                self.delete_task_form,
                                self.delete_reward_form,
                                self.habit_form,
                                self.complete_habit_form)

    def GET(self):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        username = web.cookies().get('username')
        user = user_factory.find_user(username)

        return self.render_home_page(user)


def is_snail(task):
    return isinstance(task, SnailTask)


def is_quail(task):
    return isinstance(task, QuailTask)
