#!/bin/bash

equation="\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}"

pytex2svg "$equation" -o "integral.svg"
