#!/bin/bash

pytex2svg="../tex2svg"
formula="\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}"

"$pytex2svg" "$formula" -o "integral.svg"
