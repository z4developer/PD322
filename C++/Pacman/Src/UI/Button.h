#pragma once

#include<iostream>
#include<ctime>
#include<cstdlib>
#include<sstream>

#include"SFML\System.hpp"
#include"SFML\Window.hpp"
#include"SFML\Graphics.hpp"
#include"SFML\Audio.hpp"

enum button_states { BTN_IDLE = 0, BTN_HOVER, BTN_ACTIVE };

class Button
{
private:
	short unsigned buttonState;

	sf::RectangleShape shape;
	sf::Font font;
	sf::Text text;

	sf::Color textIdleColor;
	sf::Color textHoverColor;
	sf::Color textActiveColor;
public:
	Button(float x, float y, float width, float height,
		std::string text, unsigned character_size,
		sf::Color text_idle_color, sf::Color text_hover_color, sf::Color text_active_color);
	~Button();

	
	const bool isPressed() const;


	void update(const sf::Vector2f mousePos);
	void render(sf::RenderWindow* target);
};