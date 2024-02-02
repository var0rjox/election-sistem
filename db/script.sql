insert into user(ci, name, birthdate, gender, photo, password) values('1313131', 'Alan Cosio', '1990-02-02', 'M', 'https://picsum.photos/200/300', 'alancosio');

insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('1234567', 'Pedro Pascal', '2002-05-05', 'M', 'https://picsum.photos/200/300', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('2345678', 'Maria Garcia', '1998-08-15', 'F', 'https://picsum.photos/200/300', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('3456789', 'Juan Rodriguez', '1985-03-20', 'M', 'https://picsum.photos/200/300', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('4567890', 'Ana Martinez', '1979-11-10', 'F', 'https://picsum.photos/200/300', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('5678901', 'Carlos Lopez', '1990-07-25', 'M', 'https://picsum.photos/200/300', TRUE);
insert into voter(ci, name, birthdate, gender, photo, is_enabled) values('6789012', 'Laura Hernandez', '1989-01-30', 'F', 'https://picsum.photos/200/300', TRUE);

insert into political_party(name, acronym, description, logo) values('Fuerza Juvenil', 'FJ', 'Somos el futuro del país.', 'https://picsum.photos/200/300');
insert into political_party(name, acronym, description, logo) values('Movimiento Progresista', 'MP', 'Luchamos por un cambio progresivo en la sociedad.', 'https://picsum.photos/200/300');
insert into political_party(name, acronym, description, logo) values('Partido Verde', 'PV', 'Promovemos políticas para la protección del medio ambiente.', 'https://picsum.photos/200/300');
insert into political_party(name, acronym, description, logo) values('Unión Democrática', 'UD', 'Trabajamos por la unidad y la democracia en el país.', 'https://picsum.photos/200/300');
insert into political_party(name, acronym, description, logo) values('Renovación Nacional', 'RN', 'Comprometidos con la renovación y el progreso nacional.', 'https://picsum.photos/200/300');
insert into political_party(name, acronym, description, logo) values('Partido Socialista', 'PS', 'Defendemos los derechos sociales y la igualdad para todos.', 'https://picsum.photos/200/300');

insert into political_party(name, acronym, description, logo) values('Nulo', '???', '', 'https://picsum.photos/200/300');
insert into political_party(name, acronym, description, logo) values('Blanco', '???', '', 'https://picsum.photos/200/300');

insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('141315', 'Max Fernandez', '1999-05-12', 'M', 'https://picsum.photos/200/300', 1);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('271828', 'Maria Lopez', '1985-09-20', 'F', 'https://picsum.photos/200/300', 2);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('314159', 'Juan Martinez', '1978-03-15', 'M', 'https://picsum.photos/200/300', 3);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('112358', 'Ana Ramirez', '1990-11-30', 'F', 'https://picsum.photos/200/300', 4);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('161803', 'Pedro Rodriguez', '1982-07-04', 'M', 'https://picsum.photos/200/300', 5);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('123456', 'Laura Fernandez', '1976-12-25', 'F', 'https://picsum.photos/200/300', 6);

insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('########', '111', NULL, '', '', 7);
insert into candidate(ci, name, birthdate, gender, photo, political_party_id) values('$$$$$$$$', '111', NULL, '', '', 8);