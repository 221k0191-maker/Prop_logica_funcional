
% BASE DE CONOCIMIENTOS DE CARRERAS


% Sistemas Computacionales
carrera(sistemas,
[
programacion,
matematicas,
tecnologia,
resolucion_problemas,
logica
]).

% Ciencia de Datos
carrera(ciencia_datos,
[
matematicas,
estadistica,
analisis_datos,
investigacion,
programacion
]).

% Administración
carrera(administracion,
[
liderazgo,
organizacion,
negocios,
comunicacion,
gestion
]).

% Ingeniería Industrial
carrera(industrial,
[
matematicas,
optimizacion,
procesos,
liderazgo,
analisis
]).

% Industrias Alimentarias
carrera(alimentarias,
[
quimica,
biologia,
investigacion,
calidad,
procesos
]).

% Desarrollo Comunitario
carrera(desarrollo_comunitario,
[
servicio_social,
liderazgo,
comunicacion,
trabajo_equipo,
gestion_social
]).

% Gestión Empresarial
carrera(gestion_empresarial,
[
negocios,
liderazgo,
innovacion,
emprendimiento,
gestion
]).



% REGLAS DE INFERENCIA


coincidencias([], _, 0).

coincidencias([H|T], Lista, N) :-
    member(H, Lista),
    coincidencias(T, Lista, N1),
    N is N1 + 1.

coincidencias([H|T], Lista, N) :-
    \+ member(H, Lista),
    coincidencias(T, Lista, N).

recomendar(Caracteristicas, Carrera, Puntaje) :-
    carrera(Carrera, Requisitos),
    coincidencias(Requisitos, Caracteristicas, Puntaje).