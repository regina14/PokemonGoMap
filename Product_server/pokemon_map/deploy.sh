#!/bin/bash
sudo pip freeze > requirements.text
sudo eb deploy
