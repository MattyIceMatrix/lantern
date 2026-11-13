# OP 2: NIGHT VISION

```text
             .            *           .        .         *
       *          .   NIGHT VISION        .          .
                .           ___                 *
         .                 /   \___      .            .
                    ______/  o  \__\__________
        ~~~~~~~~~~~/   [  person? 0.91  ]     \~~~~~~~~~~~~~~
      ~~~~~~~~~~~~/_____________________________\~~~~~~~~~~~~~~~
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        +-----------+
        |  >_ fps:  |    Jetson Orin Nano: TensorRT INT8
        |     28    |    "fast enough to matter, honest enough to trust"
        +-----------+
```

**Duration:** months 3–5 · **Rank on completion:** SPOTTER

## Situation

From the air or a rover camera, a person on a roof or in water is a few pixels wide. Missing one costs a life;
false alarms waste the team's time. Detection must also run on a small computer with no cloud.

## Mission

Train a person detector on search-and-rescue imagery, measure it honestly, and run it on the Jetson Orin Nano
with TensorRT.

## Recon (training reps)

```text
  [ ] NVIDIA DLI "Disaster Risk Monitoring Using Satellite Imagery" (free, about 8 h)
  [ ] Udacity computer-vision projects in the cluster map - done solo
  [ ] Read the SARD dataset paper and the FloodNet paper
  [ ] TensorRT quick-start: export ONNX -> engine, FP16 vs INT8
```

## Build

```text
  STEP 1  Data card      -> docs/cards/data-card.md for SARD (+ Corr weather variant)
  STEP 2  Split          -> train/val/test, test set frozen and never touched while tuning
  STEP 3  Train          -> a small detector (YOLO-family nano/small size)
  STEP 4  Measure        -> mAP@0.5, recall at a fixed false-alarm rate, per-condition (fog, blur)
  STEP 5  Export         -> ONNX -> TensorRT FP16 and INT8; compare accuracy loss vs speed
  STEP 6  Model card     -> docs/cards/model-card.md with what it is NOT good at
  STEP 7  Model link     -> each detection becomes a Sighting in the mission model, with confidence
```

```text
     accuracy vs speed: you must show this trade-off chart with YOUR numbers

     recall |  * FP32 (desktop)
            |      * FP16 (Jetson)
            |           * INT8 (Jetson)
            |
            +-------------------------- fps
```

## Gate: NIGHT VISION

```text
  +--------------------------------------------------------------+
  |  [ ] Test-set metrics in a results table, with hardware+date  |
  |  [ ] Recall on the "Corr" (bad weather) split reported        |
  |  [ ] INT8 engine runs on the Jetson; fps and watts measured   |
  |  [ ] Model card + data card complete                          |
  |  [ ] DLI certificate in docs/certs/                           |
  +--------------------------------------------------------------+
```

## Defend it

1. For a rescue team, is a missed person or a false alarm worse? How did that choice set your threshold?
2. Why must the test set stay frozen while you tune?
3. What did INT8 quantisation cost you in recall, and is it worth it?
4. Name one condition where your detector fails, and show an example.
