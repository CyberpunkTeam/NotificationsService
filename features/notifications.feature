Feature: CRUD Notification


  Scenario: Create notification
    Given que cree un equipo y soy owner de el

    When invito al usuario "Matias Fonseca" para que sea miembro del equipo

    Then a "Matias Fonseca" le llega una notificacion
