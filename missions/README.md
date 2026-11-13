# Mission Control

```text
    __  __ ___ ___ ___ ___ ___  _  _     ___ ___  _  _ _____ ___  ___  _
   |  \/  |_ _/ __/ __|_ _/ _ \| \| |   / __/ _ \| \| |_   _| _ \/ _ \| |
   | |\/| || |\__ \__ \| | (_) | .` |  | (_| (_) | .` | | | |   / (_) | |__
   |_|  |_|___|___/___/___\___/|_|\_|   \___\___/|_|\_| |_| |_|_\\___/|____|

        8 operations  *  14 months  *  1 kit that works when the towers go dark
```

## Campaign map

```text
                           THE AHR VALLEY, RHINELAND-PALATINATE
     N                                                                    
     ^        Bad Neuenahr-Ahrweiler                                       
     |           [OP 7 DEBRIEF]                                            
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>  to the Rhine   
            ~~                                                              
     Dernau ~~    [OP 5 BOOTS ON GROUND]      [OP 6 RELAY]                  
          ~~   Mayschoss                                                    
    Altenahr ~~~                                                            
   [OP 1 PATHFINDER]  [OP 2 NIGHT VISION]  [OP 3 RADIO SILENCE]             
       ~~                                                                   
   Schuld ~~         [OP 4 GATEKEEPER]                                      
  [OP 0 GROUNDWORK]                                                         
     ~~                                                                      
   (upstream)        ~~~  = the Ahr river                                    
```

The map is a story device, not a schedule of field trips: every operation is built and tested on the
Ahr valley map pack, from upstream (Schuld) to the mouth of the valley (Bad Neuenahr-Ahrweiler).

## The operations

| Op | Codename | Months | You come out able to... | Briefing |
| --- | --- | --- | --- | --- |
| 0 | GROUNDWORK | wk 1–3 | run a real project: repo, CI, ConOps, first requirements | [op0-groundwork.md](op0-groundwork.md) |
| 1 | PATHFINDER | 1–3 | drive a simulated rover through a flooded town and build a map | [op1-pathfinder.md](op1-pathfinder.md) |
| 2 | NIGHT VISION | 3–5 | detect people from above and run it fast on a Jetson | [op2-night-vision.md](op2-night-vision.md) |
| 3 | RADIO SILENCE | 5–7 | turn a shouted voice note into a clean situation report, fully offline | [op3-radio-silence.md](op3-radio-silence.md) |
| 4 | GATEKEEPER | 7–9 | build agents that plan sectors and a guardian that can say no | [op4-gatekeeper.md](op4-gatekeeper.md) |
| 5 | BOOTS ON GROUND | 9–11 | run the real rover in a dry field exercise | [op5-boots-on-ground.md](op5-boots-on-ground.md) |
| 6 | RELAY | 11–13 | sync to the cloud when the network returns, and show it on a dashboard | [op6-relay.md](op6-relay.md) |
| 7 | DEBRIEF | 13–14 | ship it: demo video, paper draft, talk, release | [op7-debrief.md](op7-debrief.md) |

## Rules of engagement

```text
  +------------------------------------------------------------------+
  |  1. You write the code. Claude briefs, reviews, debugs with you. |
  |  2. No gate is passed until you can DEFEND it out loud.          |
  |  3. Every number is measured on real hardware. No guesses.       |
  |  4. Failures go in the after-action review, not under the rug.   |
  |  5. Survivor data is sacred: public or synthetic data only.      |
  +------------------------------------------------------------------+
```

## How each operation runs

```text
   BRIEFING  -->  RECON  -->  BUILD  -->  GATE  -->  AAR
   (read it)     (Udacity    (code it   (pass the   (write what
                  rep +      in this    checks +    went well,
                  docs)      repo)      defend it)  what broke)
```

## Rank ladder

Pass a gate, earn the rank. Put the current rank in the README badge if you like.

```text
   OP0  [ ]  RECRUIT          OP4  [>>>>]  SECTOR LEAD
   OP1  [>]  NAVIGATOR        OP5  [>>>>>] FIELD OPERATOR
   OP2  [>>] SPOTTER          OP6  [=====] COORDINATOR
   OP3  [>>>] SIGNALLER       OP7  [*****] INCIDENT COMMANDER (of your own project)
```

## After-action review template

Copy this to `missions/aar/opN.md` at the end of each operation.

```markdown
# AAR: Op N <CODENAME>

## What we planned
## What actually happened
## Numbers (measured, with hardware and date)
## What went well (keep doing)
## What broke (and the root cause)
## What we change next op
## Requirements touched (REQ-xxx) and their test status
```
