-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-10-2020 a las 07:57:31
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `anecdotariobosques1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acudiente`
--

CREATE TABLE `acudiente` (
  `numero_documento` int(15) NOT NULL,
  `nomacudiente` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `diracudiente` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `telacudiente` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `correoacudiente` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `genero` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `acudiente`
--

INSERT INTO `acudiente` (`numero_documento`, `nomacudiente`, `diracudiente`, `telacudiente`, `correoacudiente`, `genero`) VALUES
(2221, 'Andres camargo rodriguez', 'Mz 35', '30199891010', 'dsdsd@sasas', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anotacion`
--

CREATE TABLE `anotacion` (
  `idanotacion` int(5) NOT NULL,
  `codanotacion` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `fechaanotacion` date NOT NULL,
  `descrianotacion` text COLLATE utf8_spanish_ci NOT NULL,
  `idestud` int(5) NOT NULL,
  `codprofe` int(5) NOT NULL,
  `codasignatura` int(5) NOT NULL,
  `codtipofalta` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `anotacion`
--

INSERT INTO `anotacion` (`idanotacion`, `codanotacion`, `fechaanotacion`, `descrianotacion`, `idestud`, `codprofe`, `codasignatura`, `codtipofalta`) VALUES
(35, '111', '2020-08-09', 'AAA', 4, 1, 1, 2),
(41, '1212', '1211-02-21', 'dsdsdsd', 12, 21, 21, 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignatura`
--

CREATE TABLE `asignatura` (
  `nomasignatura` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `idasignatura` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `asignatura`
--

INSERT INTO `asignatura` (`nomasignatura`, `idasignatura`) VALUES
('TIC COLEGIO', 1),
('HTML', 4),
('SENA PROGRAMACION', 6),
('QUIMICA', 7),
('SOCIALES DOMINGO', 8),
('MARKETING', 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `covidbeneficio`
--

CREATE TABLE `covidbeneficio` (
  `nombrebeneficio` varchar(35) COLLATE utf8_spanish_ci NOT NULL,
  `codigobeneficio` int(5) NOT NULL,
  `codigollave` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `covidbeneficio`
--

INSERT INTO `covidbeneficio` (`nombrebeneficio`, `codigobeneficio`, `codigollave`) VALUES
('Primaria', 1, 1),
('Bachillerato', 2, 2),
('Media', 3, 3),
('extra jis', 4, 4),
('extra segundo trimestre', 5, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eps`
--

CREATE TABLE `eps` (
  `ideps` int(5) NOT NULL,
  `nombreeps` varchar(50) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `eps`
--

INSERT INTO `eps` (`ideps`, `nombreeps`) VALUES
(1, 'Nueva EPS'),
(2, 'Medidas'),
(3, 'saludcoop'),
(4, 'colsanitas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `codestud` int(5) NOT NULL,
  `numdocestud` int(12) NOT NULL,
  `primnomestud` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `segnomestud` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `primapellestud` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `segapellestud` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `fecnacestud` date NOT NULL,
  `lugnacestud` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `gradoestud` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `direcestud` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `celestud` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `medipermestud` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `tipodocumento` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `enfermedad` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `genero` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `tipoeps` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `tiposangre` varchar(8) COLLATE utf8_spanish_ci NOT NULL,
  `idestud` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesor`
--

CREATE TABLE `profesor` (
  `tipodocprofe` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `numdocprofe` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `primapellprofe` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `segapellprofe` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `primnomprofe` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `segnomprofe` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `emailprofe` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `asignaturaprofe` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `generoprofe` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `sedeprofe` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `celprofe` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `codprofe` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `profesor`
--

INSERT INTO `profesor` (`tipodocprofe`, `numdocprofe`, `primapellprofe`, `segapellprofe`, `primnomprofe`, `segnomprofe`, `emailprofe`, `asignaturaprofe`, `generoprofe`, `sedeprofe`, `celprofe`, `codprofe`) VALUES
('Cedula', 'ddsdsd', 'dsdsds', 'PRUEBA', 'Andres camargo rodri', 'sdsds', 'rockoami@gmail.com', 'sdsdsdsdds', 'Masculino', 'DAsas', 'dsdsdsd', 142),
('Cedula', 'ddsdsd', 'dsdsds', 'PRUEBA', 'Andres camargo rodri', 'sdsdsd', 'rockoami@gmail.com', 'sddsdd', 'Masculino', 'DAsas', 'ADAS', 2311),
('Cedula', 'sddsd', 'sdsds', 'dsdsd', 'sdsds', 'dsd', 'rockoami@gmail.com', 'sdsdsdsdds', 'Masculino', 'dsdsdsdsd', 'dsdsd', 3232);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipodocumento`
--

CREATE TABLE `tipodocumento` (
  `idtipodoc` int(5) NOT NULL,
  `nomtipodoc` varchar(30) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tipodocumento`
--

INSERT INTO `tipodocumento` (`idtipodoc`, `nomtipodoc`) VALUES
(1, 'Tarjeta de identidad'),
(2, 'Cédula de ciudadania'),
(3, 'Tarjeta de extranjeria'),
(4, 'Pasaporte'),
(5, 'Pasaporte comunitario'),
(6, 'aaaaa'),
(7, 'AMERICANO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipoenfermedad`
--

CREATE TABLE `tipoenfermedad` (
  `idtipoenfermedad` int(5) NOT NULL,
  `nomtipoenfermedad` varchar(40) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tipoenfermedad`
--

INSERT INTO `tipoenfermedad` (`idtipoenfermedad`, `nomtipoenfermedad`) VALUES
(1, 'Enfermedades cardiovasculares'),
(2, 'Obesidad'),
(3, 'Diabetes'),
(4, 'Gripa'),
(5, 'Cardiovascular'),
(6, 'aaaaaa'),
(7, 'TTTTTTT');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipofalta`
--

CREATE TABLE `tipofalta` (
  `idtipofalta` int(5) NOT NULL,
  `nomtipofalta` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `descriptipofalta` text COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tipofalta`
--

INSERT INTO `tipofalta` (`idtipofalta`, `nomtipofalta`, `descriptipofalta`) VALUES
(1, 'leve', 'Porte del uniform'),
(2, 'Grave', 'Faltas recurrentes sin excusa'),
(3, 'Gravísima', 'Enfrentamiento con compañeros'),
(4, 'Reiterativa', 'Para docentes y directivos'),
(5, 'aaaa', 'AAAAAA'),
(6, 'BBBB', 'BBBBB'),
(7, 'dda', 'sdsdsdsds'),
(8, 'dda', 'sdsdsdsds'),
(9, 'dda', 'sdsdsdsds'),
(10, 'dda', 'sdsdsdsds'),
(3214, 'dda', 'sdsdsdsds');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipogenero`
--

CREATE TABLE `tipogenero` (
  `idgenero` int(5) NOT NULL,
  `nomtipogenero` varchar(30) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tipogenero`
--

INSERT INTO `tipogenero` (`idgenero`, `nomtipogenero`) VALUES
(1, 'Masculino'),
(2, 'Femenino'),
(3, 'No Identificado'),
(4, 'xxxx'),
(5, 'yyyyyy'),
(6, 'aaaa'),
(7, 'WWWW');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiposangre`
--

CREATE TABLE `tiposangre` (
  `nomtiposangre` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `idtiposangre` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `tiposangre`
--

INSERT INTO `tiposangre` (`nomtiposangre`, `idtiposangre`) VALUES
('A+-', 68);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acudiente`
--
ALTER TABLE `acudiente`
  ADD PRIMARY KEY (`numero_documento`);

--
-- Indices de la tabla `anotacion`
--
ALTER TABLE `anotacion`
  ADD PRIMARY KEY (`idanotacion`),
  ADD KEY `idestud1` (`idestud`),
  ADD KEY `codprofe` (`codprofe`),
  ADD KEY `codasignatura` (`codasignatura`),
  ADD KEY `codtipofalta` (`codtipofalta`);

--
-- Indices de la tabla `asignatura`
--
ALTER TABLE `asignatura`
  ADD PRIMARY KEY (`idasignatura`);

--
-- Indices de la tabla `covidbeneficio`
--
ALTER TABLE `covidbeneficio`
  ADD PRIMARY KEY (`codigollave`);

--
-- Indices de la tabla `eps`
--
ALTER TABLE `eps`
  ADD PRIMARY KEY (`ideps`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`idestud`),
  ADD KEY `tipodocumento` (`tipodocumento`),
  ADD KEY `tipoenfermedad1` (`enfermedad`),
  ADD KEY `tipogenero1` (`genero`),
  ADD KEY `tipoeps1` (`tipoeps`),
  ADD KEY `tiposangre` (`tiposangre`);

--
-- Indices de la tabla `profesor`
--
ALTER TABLE `profesor`
  ADD PRIMARY KEY (`codprofe`);

--
-- Indices de la tabla `tipodocumento`
--
ALTER TABLE `tipodocumento`
  ADD PRIMARY KEY (`idtipodoc`);

--
-- Indices de la tabla `tipoenfermedad`
--
ALTER TABLE `tipoenfermedad`
  ADD PRIMARY KEY (`idtipoenfermedad`);

--
-- Indices de la tabla `tipofalta`
--
ALTER TABLE `tipofalta`
  ADD PRIMARY KEY (`idtipofalta`);

--
-- Indices de la tabla `tipogenero`
--
ALTER TABLE `tipogenero`
  ADD PRIMARY KEY (`idgenero`);

--
-- Indices de la tabla `tiposangre`
--
ALTER TABLE `tiposangre`
  ADD PRIMARY KEY (`idtiposangre`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `acudiente`
--
ALTER TABLE `acudiente`
  MODIFY `numero_documento` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2222;

--
-- AUTO_INCREMENT de la tabla `anotacion`
--
ALTER TABLE `anotacion`
  MODIFY `idanotacion` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de la tabla `asignatura`
--
ALTER TABLE `asignatura`
  MODIFY `idasignatura` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `eps`
--
ALTER TABLE `eps`
  MODIFY `ideps` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `idestud` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipodocumento`
--
ALTER TABLE `tipodocumento`
  MODIFY `idtipodoc` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `tipoenfermedad`
--
ALTER TABLE `tipoenfermedad`
  MODIFY `idtipoenfermedad` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `tipofalta`
--
ALTER TABLE `tipofalta`
  MODIFY `idtipofalta` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3215;

--
-- AUTO_INCREMENT de la tabla `tipogenero`
--
ALTER TABLE `tipogenero`
  MODIFY `idgenero` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `tiposangre`
--
ALTER TABLE `tiposangre`
  MODIFY `idtiposangre` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `anotacion`
--
ALTER TABLE `anotacion`
  ADD CONSTRAINT `anotacion_ibfk_4` FOREIGN KEY (`codtipofalta`) REFERENCES `tipofalta` (`idtipofalta`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
