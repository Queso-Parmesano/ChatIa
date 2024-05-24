
CREATE DATABASE chatia;
USE chatia;

CREATE TABLE `chats` (
  `idChat` int(11) NOT NULL,
  `idUser` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `chats` (`idChat`, `idUser`, `name`) VALUES
(1, 1, 'chat 1'),
(2, 1, 'chat 2'),
(3, 2, 'chat 3'),
(4, 2, 'chat 4'),
(5, 3, 'chat 5'),
(6, 3, 'chat 6'),
(7, 3, 'chat 7');

CREATE TABLE `mensajes` (
  `idChat` int(11) DEFAULT NULL,
  `msjUser` varchar(9999) DEFAULT NULL,
  `msjIa` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(49) DEFAULT NULL,
  `passw` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `usuarios` (`id`, `username`, `passw`) VALUES
(1, 'test1', 'f1f836bfd94f5181c992d98f161e292c4bafc398922941faf2853927c8170d10'),
(2, 'test2', 'f1f836bfd94f5181c992d98f161e292c4bafc398922941faf2853927c8170d10'),
(3, 'test3', 'f1f836bfd94f5181c992d98f161e292c4bafc398922941faf2853927c8170d10');

ALTER TABLE `chats`
  ADD PRIMARY KEY (`idChat`),
  ADD KEY `chats_ibfk_1` (`idUser`);

ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `chats`
  MODIFY `idChat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `chats`
  ADD CONSTRAINT `chats_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `usuarios` (`id`);
COMMIT;
