from django.http import HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from common.decorators import player_required
from .service import SpinGameError, play_spin


@method_decorator(player_required, 'dispatch')
class PlaySpinsView(TemplateView):
    template_name = 'spin/spin.html'

    def post(self, request, *args, **kwargs):
        if not request.user.is_player():
            return HttpResponseBadRequest('Only players can play.')

        context = self.get_context_data(**kwargs)

        try:
            game = play_spin(request.user.player)
            context.update(
                game=game,
                error=False,
            )
        except SpinGameError as e:
            context.update(
                error=True,
                message=e.message,
            )

        return self.render_to_response(context)
