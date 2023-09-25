#https://www.twilio.com/docs/voice/twiml
from twilio.rest import Client


account_SID = 'ACf4f78fb9da80642f444b4df7cff634d1'
auth_toke="26b8d26dfe26721b7e322e0d15eb0169"
meu_nr= "+258 84 738 8489"
nr_twilio="+12626762524"

client=Client(account_SID,auth_toke)

mensagem='''
<response>
<Say>
Olá, tudo bem? conta boa coisa desse lado.
até a ligação está automatizado, desculpa aí.
</Say>
</response>

'''
ligacao=client.calls.create(
    to=meu_nr,
    from_=nr_twilio,
    twiml=mensagem
)