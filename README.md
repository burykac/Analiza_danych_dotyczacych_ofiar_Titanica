# Analiza_danych_dotyczacych_ofiar_Titanica

Analizę danych ofiar Titanica zacząłem od pozbycia się z pliku informacji niekoniecznie przydatnych do znalezienia
odpowiedzi na postawione pytanie: Co mogło mieć wpływ na przeżycie pasażerów? 
W celu odpowiedzenia na to pytanie należy najpierw zadać pytanie: Ile osób przeżyło, a ile zginęło? 

df = train_file["Survived"].sum()
sns.catplot(data=train_file, x="Survived", kind="count")
plt.show()
print(df)

Jak widać na zwracanym przez powyższy kod wykresie z 891 zarejestrowanych osób przeżyło ich 342. 

Czy występowała zatem zależność pod względem klasy biletu zakupionego przez pasażera,a przeżywalnością?

sns.catplot(data=train_file, x="Pclass",  kind="count", hue="Survived")
plt.show()

Wykres wyświetlany przez powyższy kod sugeruje raczej większe prawdopodobieńtwo przeżycia, w zależności od kupionego
biletu, czy raczej, wybranej klasy podróży. Pasażerowie klasy pierwszej przeżyli w większości podczas gdy większość 
pasażerów klasy trzeciej zginęła.
Na wykresie prezentującym zależność między wiekiem, ceną biletu a przeżywalnością widzimy dane sugerujące, że 
osoby, które przeżyły w klasie niższej to były dzieci, podczas gdy wraz z ceną biletu wiek jednostki, która przeżyła 
rośnie. Widać to w wykresie prezentowanym przez kod poniżej.

sns.relplot(data=train_file, x="Fare", y="Age", hue="Survived")
plt.show()

Jak zatem prezentuje się przeżywalność jednostki w zależności od samego wieku?

sns.kdeplot(data=train_file, x="Age", hue="Survived")
plt.show()

Większość dzieci przeżyła, zatem można śmiało wnioskować, że dzieci miały pierwszeństwo przy ewakuacji. 
Skoro wiemy już, że priorytetowo ewakuowane były dzieci, to sprawdźmy kto był priorytetyzowany jeśli chodzi o płeć,
kobiety czy mężczyźni?

sns.catplot(data=train_file, x="Sex", hue="Survived", kind="count")
plt.show()

Jak widać na wykresie zdecydowana większość kobiet przeżyła. Było wśród nich nie tylko więcej uratowanych osób, ale też 
stanowią one ponad połowę uratowanych osób.

Podumowując przeanalizowane dane, można wysunąć następujące wnioski:

1. Ewakuując załogę pierwszeństwo otrzymały dzieci oraz kobiety.
2. Osoby podróżujące wyższą klasą miały większe szanse na przeżycie. Osoby ocalone podróżujące wyższą klasą były
w średnim wieku.

