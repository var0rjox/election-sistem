insert into user(ci, name, birthdate, gender, photo, password) values('1313131', 'Alan Cosio', '1990-02-02', 'M', '', 'alancosio');

-- Voters
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('1234567', 'Pedro Pascal', '2002-05-05', 'M', '', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('2345678', 'Maria Garcia', '1998-08-15', 'F', '', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('3456789', 'Juan Rodriguez', '1985-03-20', 'M', '', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('4567890', 'Ana Martinez', '1979-11-10', 'F', '', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('5678901', 'Carlos Lopez', '1990-07-25', 'M', '', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('6789012', 'Laura Hernandez', '1989-01-30', 'F', '', TRUE);

-- Political parties
insert into political_party(name, acronym, description, logo) values('Fuerza Juvenil', 'FJ', 'Somos el futuro del país.', '');
insert into political_party(name, acronym, description, logo) values('Movimiento Progresista', 'MP', 'Luchamos por un cambio progresivo en la sociedad.', '');
insert into political_party(name, acronym, description, logo) values('Partido Verde', 'PV', 'Promovemos políticas para la protección del medio ambiente.', '');
insert into political_party(name, acronym, description, logo) values('Unión Democrática', 'UD', 'Trabajamos por la unidad y la democracia en el país.', '');
insert into political_party(name, acronym, description, logo) values('Renovación Nacional', 'RN', 'Comprometidos con la renovación y el progreso nacional.', '');
insert into political_party(name, acronym, description, logo) values('Partido Socialista', 'PS', 'Defendemos los derechos sociales y la igualdad para todos.', '');

insert into political_party(name, acronym, description, logo) values('Nulo', '???', '', '');
insert into political_party(name, acronym, description, logo) values('Blanco', '???', '', '');

-- Candidates
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('141315', 'Max Fernandez', '1999-05-12', 'M', '', 1);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('271828', 'Maria Lopez', '1985-09-20', 'F', '', 2);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('314159', 'Juan Martinez', '1978-03-15', 'M', '', 3);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('112358', 'Ana Ramirez', '1990-11-30', 'F', '', 4);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('161803', 'Pedro Rodriguez', '1982-07-04', 'M', '', 5);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('123456', 'Laura Fernandez', '1976-12-25', 'F', '', 6);

insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('########', '111', NULL, '', '', 7);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('$$$$$$$$', '111', NULL, '', '', 8);