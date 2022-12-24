Feature: CRUD Notification


  Scenario: Create notification
    Given que cree un equipo y soy owner de el

    When invito al usuario "Matias Fonseca" para que sea miembro del equipo

    Then a "Matias Fonseca" le llega una notificacion de invitacion a equipo

  Scenario: Update notification
    Given que recibi una notificacion

    When cuando la abro

    Then se marca como vista
